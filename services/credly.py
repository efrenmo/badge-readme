# from bs4 import BeautifulSoup
# import lxml, requests

# from settings import (
#     CREDLY_SORT,
#     CREDLY_USER,
#     CREDLY_BASE_URL,
#     BADGE_SIZE,
#     NUMBER_LAST_BADGES,
# )


# class Credly:
#     def __init__(self, f=None):
#         self.FILE = f
#         self.BASE_URL = CREDLY_BASE_URL
#         self.USER = CREDLY_USER
#         self.SORT = CREDLY_SORT

#         print(self.BASE_URL, self.USER, self.SORT)

#     def data_from_html(self):
#         if self.FILE:
#             with open(self.FILE, "r") as f:
#                 return f.read()
#         url = f"{self.BASE_URL}/users/{self.USER}/badges?sort={self.sort_by()}"
#         response = requests.get(url)

#         return response.text

#     def sort_by(self):
#         return "most_popular" if self.SORT == "POPULAR" else "-state_updated_at"

#     # def convert_to_dict(self, htmlBadge):
#     #     soupBadge = BeautifulSoup(str(htmlBadge), "lxml")
#     #     img = soupBadge.findAll(
#     #         "img", {"class": "cr-standard-grid-item-content__image"}
#     #     )[0]
#     #     return {
#     #         "title": str(htmlBadge["title"]).replace('"', '\\"'),
#     #         "href": self.BASE_URL + htmlBadge["href"],
#     #         "img": img["src"].replace("110x110", f"{BADGE_SIZE}x{BADGE_SIZE}"),
#     #     }

#     def convert_to_dict(self, htmlBadge):
#         soupBadge = BeautifulSoup(str(htmlBadge), "lxml")
#         img = soupBadge.findAll("img", {"class": "cr-standard-grid-item-content__image"})[0]
#         original_url = img["src"]
#         resized_url = original_url.replace("110x110", f"{BADGE_SIZE}x{BADGE_SIZE}")
#         return {
#             "title": str(htmlBadge["title"]).replace('"', '\\"'),
#             "href": self.BASE_URL + htmlBadge["href"],
#             "img": resized_url,
#             "original_img": original_url  # Keep the original URL as a fallback
#         }
    
#     def return_badges_html(self):
#         data = self.data_from_html()
#         soup = BeautifulSoup(data, "lxml")
#         return soup.findAll("a", {"class": "cr-public-earned-badge-grid-item"})

#     # def generate_md_format(self, badges):
#     #     if not badges:
#     #         return None
#     #     return "\n".join(
#     #         map(
#     #             lambda it: f"[![{it['title']}]({it['img']})]({it['href']} \"{it['title']}\")",
#     #             badges,
#     #         )
#     #     )

#     ###### 2
#     # def generate_md_format(self, badges):
#     # if not badges:
#     #     return None
#     # return "\n".join(
#     #     map(
#     #         # lambda it: f'<a href="{it["href"]}" title="{it["title"]}"><img src="{it["img"]}" width="{BADGE_SIZE}" height="{BADGE_SIZE}" alt="{it["title"]}"></a>',
#     #         # badges,
#     #         lambda it: f'<a href="{it["href"]}" title="{it["title"]}"><img src="{it["img"]}" width="110" height="110" alt="{it["title"]}"></a>',
#     #         badges,
#     #     )
#     # )


#     ##### 3

#     # def generate_md_format(self, badges):
#     # if not badges:
#     #     return None
#     # return "\n".join(
#     #     map(
#     #         lambda it: f'[![{it["title"]}]({it["img"]})]({it["href"]} "{it["title"]}")<!-- {{"width":"110px","height":"110px"}} -->',
#     #         badges,
#     #     )
#     # )
    
#     #### 4

#    def generate_md_format(self, badges):
#         if not badges:
#             return None
#         return "\n".join(
#             map(
#                 lambda it: f'<a href="{it["href"]}" title="{it["title"]}"><img src="{it["img"]}" width="100" height="100" alt="{it["title"]}"></a>',
#                 badges,
#             )
#         )
    
#     def get_markdown(self):
#         badges_html = (
#             self.return_badges_html()[0:NUMBER_LAST_BADGES]
#             if NUMBER_LAST_BADGES > 0
#             else self.return_badges_html()
#         )
#         return self.generate_md_format(
#             [self.convert_to_dict(badge) for badge in badges_html]
#         )




from bs4 import BeautifulSoup
import lxml, requests

from settings import (
    CREDLY_SORT,
    CREDLY_USER,
    CREDLY_BASE_URL,
    BADGE_SIZE,
    NUMBER_LAST_BADGES,
)


class Credly:
    def __init__(self, f=None):
        self.FILE = f
        self.BASE_URL = CREDLY_BASE_URL
        self.USER = CREDLY_USER
        self.SORT = CREDLY_SORT

        print(self.BASE_URL, self.USER, self.SORT)

    def data_from_html(self):
        if self.FILE:
            with open(self.FILE, "r") as f:
                return f.read()
        url = f"{self.BASE_URL}/users/{self.USER}/badges?sort={self.sort_by()}"
        response = requests.get(url)

        return response.text

    def sort_by(self):
        return "most_popular" if self.SORT == "POPULAR" else "-state_updated_at"

    def convert_to_dict(self, htmlBadge):
        soupBadge = BeautifulSoup(str(htmlBadge), "lxml")
        img = soupBadge.findAll("img", {"class": "cr-standard-grid-item-content__image"})[0]
        original_url = img["src"]
        resized_url = original_url.replace("110x110", f"{BADGE_SIZE}x{BADGE_SIZE}")
        return {
            "title": str(htmlBadge["title"]).replace('"', '\\"'),
            "href": self.BASE_URL + htmlBadge["href"],
            "img": resized_url,
            "original_img": original_url  # Keep the original URL as a fallback
        }
    
    def return_badges_html(self):
        data = self.data_from_html()
        soup = BeautifulSoup(data, "lxml")
        return soup.findAll("a", {"class": "cr-public-earned-badge-grid-item"})

    # def generate_md_format(self, badges):
    #     if not badges:
    #         return None
    #     return "\n".join(
    #         map(
    #             lambda it: f'<a href="{it["href"]}" title="{it["title"]}"><img src="{it["img"]}" width="100" height="100" alt="{it["title"]}"></a>',
    #             badges,
    #         )
    #     )

    def generate_md_format(self, badges):
        if not badges:
            return None
        return "\n".join(
            map(
                lambda it: f'<img src="{it["img"]}" width="100" height="100" alt="{it["title"]}" style="background: transparent !important;">',
                badges,
            )
        )
    
    def get_markdown(self):
        badges_html = (
            self.return_badges_html()[0:NUMBER_LAST_BADGES]
            if NUMBER_LAST_BADGES > 0
            else self.return_badges_html()
        )
        return self.generate_md_format(
            [self.convert_to_dict(badge) for badge in badges_html]
        )
