import requests
import wikipediaapi


USER_AGENT = "AaravWikipediaResearchAssistant/1.0 (student project)"
wiki = wikipediaapi.Wikipedia(
    user_agent=USER_AGENT,
    language="en"
)


def search_wikipedia(query):
    """Search Wikipedia for pages related to the query."""
    
    url = "https://en.wikipedia.org/w/api.php"

    params = {
        "action": "query",
        "list": "search",
        "srsearch": query,
        "format": "json",
        "srlimit": 5
    }

    response = requests.get(
        url,
        params=params,
        headers={"User-Agent": USER_AGENT},
        timeout=10
    )

    response.raise_for_status()

    data = response.json()

    return [
        result["title"]
        for result in data["query"]["search"]
    ]


def research_assistant():
    print("🔎 Welcome to the Wikipedia Research Assistant!")

    while True:
        query = input(
            "\nEnter a topic to search (or type 'exit' to quit): "
        ).strip()

        if query.lower() == "exit":
            print("👋 Goodbye!")
            break

        try:
            # Get the Wikipedia page
            page = wiki.page(query)

            if not page.exists():
                print("\n❌ No exact page found. Here are some suggestions:")

                suggestions = search_wikipedia(query)

                if suggestions:
                    for i, topic in enumerate(suggestions, start=1):
                        print(f"   {i}. {topic}")
                else:
                    print("   No related topics found.")

                continue

            # Display summary
            summary = page.summary

            # Limit to approximately five sentences
            sentences = summary.split(". ")
            short_summary = ". ".join(sentences[:5])

            if len(sentences) > 5:
                short_summary += "."

            print(f"\n📚 Summary of '{page.title}':\n")
            print(short_summary)

            # Show related topics
            suggestions = search_wikipedia(query)

            if suggestions:
                print("\n📌 Related Topics You Might Be Interested In:")

                for i, topic in enumerate(suggestions[:5], start=1):
                    if topic != page.title:
                        print(f"   {i}. {topic}")

        except requests.RequestException:
            print("\n🌐 Could not connect to Wikipedia. Please check your internet connection.")

        except Exception as e:
            print(f"\n🚨 An unexpected error occurred: {e}")


if __name__ == "__main__":
    research_assistant()