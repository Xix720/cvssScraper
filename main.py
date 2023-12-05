from vulInfo import CvssBoxScraper
import os


def generate_cve_url(cve_number):
    base_url = "https://www.cvedetails.com/cve/"
    return f"{base_url}{cve_number}/?q={cve_number}"


def process_cve_file(file_path):
    print("正在解析cve列表")

    urlList = []
    try:
        with open(file_path, 'r') as file:
            print("正在生成url列表")
            for line in file:
                cve_number = line.strip()
                cve_url = generate_cve_url(cve_number)
                urlList.append(cve_url)
        print("url列表生成完毕")
        return urlList
    except FileNotFoundError:
        print(f"文件 '{file_path}' 未找到")
    except Exception as e:
        print(f"发生错误: {e}")


if __name__ == "__main__":
    filePath_C = "Lists/Vul_C.csv"
    filePath_Java = "Lists/Vul_Java.csv"

    urlList_C = process_cve_file(filePath_C)
    urlList_Java = process_cve_file(filePath_Java)

    # scraper_C = CvssBoxScraper(urlList_C)
    # scoreList_C = scraper_C.get_cvss_score_10()
    #
    # if scoreList_C:
    #     for x in scoreList_C:
    #         print(x)
    #     result_folder = "Result"
    #     file_path = os.path.join(result_folder, "output_C.txt")
    #
    #     with open(file_path, 'w') as file:
    #         for index, item in enumerate(scoreList_C):
    #             file.write(f"{item}\n")
    #
    #     print(f"List has been saved to {file_path}")

    scraper_Java = CvssBoxScraper(urlList_Java)
    scoreList_Java = scraper_Java.get_cvss_score_10()

    if scoreList_Java:
        for x in scoreList_Java:
            print(x)
        result_folder = "Result"
        file_path = os.path.join(result_folder, "output_Java.txt")

        with open(file_path, 'w') as file:
            for index, item in enumerate(scoreList_Java):
                file.write(f"{item}\n")

        print(f"List has been saved to {file_path}")
