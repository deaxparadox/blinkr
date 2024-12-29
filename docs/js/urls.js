/*

This function demonstrate, how to parse the URL for getting
the query string (or path query parameters) from the URL.

*/
const getQueryString = async () => {
    // Parse the current URL.
    const myParams = new URLSearchParams(window.location.search);

    // Search the query key.
    // 
    // Here will searched for "last" and "short_active".
    const last = myParams.get("last");
    const shortActive = myParams.get("short_active");

    // Action based on query strings.
    if (last === "yes" && shortActive === "yes") {
        const short_url = document.querySelector(".lew-short-url").innerText;
        return short_url
    }
}