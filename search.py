#!/usr/bin/env python3
import webbrowser
import sys

# a script to do internet searches from the terminal

# steps
# decide the search engine
# for each search argument
#   form a structured query and search in a new tab


# dictionary containing the base queries of all the search engines
baseQueries = {
    "google": "https://www.google.com/search?q=",
    "youtube": "https://www.youtube.com/results?search_query="
}


def makeQueries(baseQuery, joiningChar):
    """
    Funtion to process queries

    Parameters:
        baseQuery(string): base query specific to the search engine  
        joiningChar(string): the string used to join saperate terms in the query
    Returns:
        result(list[(string)]): a list of structured queries

    """
    result = []
    for query in sys.argv[2:]:  # for every individual query
        queryList = query.split()  # split individual terms in a query
        # join them back with the joining char between them
        formatedQuery = joiningChar.join(queryList)
        # append the structured query to the result
        result.append(baseQuery + formatedQuery)
    return result


def openTabs(allQueries):
    for query in allQueries:
        # print(query)
        webbrowser.open_new_tab(query)


def main():
    baseQuery = ""
    # selecting the correct base querie
    engine = sys.argv[1]
    baseQuery = baseQueries[engine]

    allQueries = []
    allQueries = makeQueries(baseQuery, "%20")
    # print(allQueries, end="\n")
    openTabs(allQueries)


if __name__ == "__main__":
    main()
