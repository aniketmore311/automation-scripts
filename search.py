#!/usr/bin/env python3
import webbrowser
import sys

# a script to do internet searches from the terminal

# example
# $ ./search google "search one" "search two"
# this will open 2 tabs with google searches "search one" and "search two"

# steps
# decide the search engine
# for each search argument
#   form a structured query and search in a new tab


# dictionary containing the base queries and joining characters of all the search engines
baseQueries = {
    "google": ["https://www.google.com/search?q=", "%20"],
    "youtube": ["https://www.youtube.com/results?search_query=", "%20"],
    "cppref": ["https://en.cppreference.com/mwiki/index.php?title=Special%3ASearch&search=", "+"],
    "stacko": ["https://stackoverflow.com/search?q=", "+"]
}


def makeQueries(baseQuery, joiningChar):
    """
    Funtion to process search queries

    Parameters:
        baseQuery(string): base query specific to the search engine
        joiningChar(string): the string used to join saperate terms in the query
    Returns:
        result(list[(string)]): a list of structured queries

    """
    results = []
    searchQueries = sys.argv[2:]
    for query in searchQueries:  # for every individual query
        queryList = query.split()  # split individual terms in a query
        # join them back with the joining char between them
        formatedQuery = joiningChar.join(queryList)
        # append the structured query to the result
        results.append(baseQuery + formatedQuery)
    return results


def openTabs(allQueries):
    for completeQuery in allQueries:
        # print(query)
        webbrowser.open_new_tab(completeQuery)


def main():
    # selecting the correct base querie
    engine = sys.argv[1]
    baseQuery = baseQueries[engine][0]
    joiningChar = baseQueries[engine][1]

    allQueries = []
    allQueries = makeQueries(baseQuery, joiningChar)
    # print(allQueries, end="\n")
    openTabs(allQueries)


if __name__ == "__main__":
    main()
