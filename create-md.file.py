   # md_file_content = f"# Earnings on {earnings_date}\n\n"

    # md_file_content += "| Symbol | Link |\n"
    # md_file_content += "| ---| --- |\n"

    # md_companies_table = [
    #     f"| {company} | https://namuan.github.io/lazy-trader/?symbol={company} |"
    #     for company in companies_list
    # ]
    # md_file_content += "\n".join(md_companies_table)
    # earnings_output_folder = Path().cwd().joinpath("docs").joinpath("earnings")
    # earnings_output_folder.mkdir(parents=True, exist_ok=True)
    # earnings_output_folder.joinpath(f"earnings-{earnings_date}.md").write_text(
    #     md_file_content
    # )