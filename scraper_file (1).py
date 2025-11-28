import requests
from bs4 import BeautifulSoup
import pandas as pd
import re
import time

BASE = "https://nitj.irins.org"
HEADERS = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
}

#basic fetch karo
def fetch_html(url: str) -> str:
    resp = requests.get(url, headers=HEADERS)
    resp.raise_for_status()
    return resp.text


#All depts
def get_all_departments():
    url = "https://nitj.irins.org/"
    html = fetch_html(url)
    soup = BeautifulSoup(html, "lxml")

    departments = []

    for a in soup.select("a[href*='/faculty/index/Department']"):
        name = a.get_text(strip=True)
        dept_url = a.get("href")

        if not dept_url.startswith("http"):
            dept_url = BASE + dept_url

        departments.append({
            "dept_name": name,
            "dept_url": dept_url
        })

    return departments
#Faculty of department
def get_faculty_from_department(dept):
    html = fetch_html(dept["dept_url"])
    soup = BeautifulSoup(html, "lxml")

    faculty_rows = []

    for card in soup.select(".flat-testimonials-in"):
        name_tag = card.select_one("h3")
        desig_tag = card.select_one("span.color-lightYellow")
        profile_link_tag = card.select_one("a[href*='/profile/']")

        if not name_tag or not profile_link_tag:
            continue

        name = name_tag.get_text(strip=True)
        designation = desig_tag.get_text(strip=True) if desig_tag else None

        profile_url = profile_link_tag.get("href")
        if not profile_url.startswith("http"):
            profile_url = BASE + profile_url

        faculty_rows.append({
            "name": name,
            "designation": designation,
            "department": dept["dept_name"],
            "profile_url": profile_url
        })

    return faculty_rows


#scraping profile data
def parse_profile_metrics(url):
    html = fetch_html(url)
    soup = BeautifulSoup(html, "lxml")
    text = soup.get_text(" ", strip=True)

    data = {
        "vidwan_id": None,
        "orcid_id": None,
        "scopus_id": None,
        "researcher_id": None,
        "gscholar_id": None,
        "total_publications": None,
        "citations_total": None,
        "h_index": None,
        "coauthor_count": None,
        "i10_index": None,
        "expertise": None,
    }

    #VIDWAN ID
    m = re.search(r"Vidwan-ID\s*:\s*(\d+)", text)
    if m:
        data["vidwan_id"] = m.group(1)

    #GENERIC IDs
    def get_id_after(label_regex):
        tag = soup.find(string=re.compile(label_regex, re.I))
        if tag:
            a = tag.find_next("a")
            if a:
                return a.get_text(strip=True)
        return None

    data["orcid_id"] = get_id_after(r"Orcid Id")
    data["scopus_id"] = get_id_after(r"Scopus Id")
    data["researcher_id"] = get_id_after(r"Researcher Id")

    #GOOGLE SCHOLAR ID 
    scholar_block = soup.find("span", id="i_google_sid")
    if scholar_block:
        a = scholar_block.find("a")
        if a:
            url_link = a.get("href", "")
            m = re.search(r"user=([\w-]+)", url_link)
            if m:
                data["gscholar_id"] = m.group(1)
            else:
                data["gscholar_id"] = a.get_text(strip=True)

    #TOTAL PUBLICATIONS
    pub = soup.select_one("ul.faculty_profile_count li a")
    if pub:
        text_val = pub.get_text(strip=True)
        num = text_val.split()[0]
        if num.isdigit():
            data["total_publications"] = int(num)
    else:
        m_pub = re.search(r"Publications\s*\((\d+)\)", text)
        if m_pub:
            data["total_publications"] = int(m_pub.group(1))

    #TOTAL CITATIONS
    citation_span = soup.find(lambda tag: tag.name == "span" and tag.get("class") and "counter" in tag.get("class"))
    if citation_span:
        try:
            data["citations_total"] = int(citation_span.get_text(strip=True))
        except:
            pass

    # H-INDEX
    m_h = re.search(r"(\d+)\s*h-index", text, re.I)
    if m_h:
        data["h_index"] = int(m_h.group(1))

    #CO-AUTHOR COUNT
    co_btn = soup.find(lambda tag: tag.name == "button" and "Co-author" in tag.get_text())
    if co_btn:
        txt = co_btn.get_text(" ", strip=True)
        m = re.search(r"Co-?author\s*[-:–]\s*(\d+)", txt)
        if m:
            data["coauthor_count"] = int(m.group(1))

    #i10 INDEX
    i10_title = soup.find(lambda tag:
        tag.name == "h5" and "i-10" in tag.get_text(strip=True).lower()
    )

    if i10_title:
        next_div = i10_title.find_next("div", class_="citation_half")
        if next_div:
            span = next_div.find("span", class_="counter")
            if span:
                try:
                    data["i10_index"] = int(span.get_text(strip=True))
                except:
                    pass

    # expertise
    exp_span = soup.find("span", id="e_expertise")
    if exp_span:
        data["expertise"] = exp_span.get_text(strip=True)

    return data


#main function
def main():
    print("Fetching department list...")
    departments = get_all_departments()
    print(f"Found {len(departments)} departments.")

    all_rows = []

    for dept in departments:
        print(f"\n=== Department: {dept['dept_name']} ===")
        faculty_list = get_faculty_from_department(dept)
        print(f"  Found {len(faculty_list)} faculty")

        for fac in faculty_list:
            print(f"   -> Scraping: {fac['name']}")
            metrics = parse_profile_metrics(fac["profile_url"])
            row = {**fac, **metrics}
            all_rows.append(row)
            time.sleep(1)

    df = pd.DataFrame(all_rows)
    df.to_csv("nitj_data.csv", index=False, encoding="utf-8-sig")

    print("\nSaved to nitj_data.csv")
    print("Total faculty scraped:", len(all_rows))


if __name__ == "__main__":
    main()
