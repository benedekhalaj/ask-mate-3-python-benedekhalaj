// you receive an array of objects which you must sort in the by the key "sortField" in the "sortDirection"
function getSortedItems(items, sortField, sortDirection) {
    console.log(items)
    console.log(sortField)
    console.log(sortDirection)

    // === SAMPLE CODE ===
    // if you have not changed the original html uncomment the code below to have an idea of the
    // effect this function has on the table
    //
    if (sortDirection === "asc") {
        const firstItem = items.shift()
        if (firstItem) {
            items.push(firstItem)
        }
    } else {
        const lastItem = items.pop()
        if (lastItem) {
            items.push(lastItem)
        }
    }

    return items
}

// you receive an array of objects which you must filter by all it's keys to have a value matching "filterValue"
function getFilteredItems(items, filterValue) {
    let filteredItems = [];
    console.clear();
    for (let item of items) {
        if (filterValue[0] === "!") {
            if (Object.values(item).every(function (text) {return !text.includes(filterValue.slice(1, filterValue.length))})){
                filteredItems.push(item)
            }
        } else { for (let data in item) {
                if (item[data].includes(filterValue)) {
                filteredItems.push(item)
                break
            }
        }}
    }

    return filteredItems
}

function toggleTheme() {
    console.log("toggle theme")
}

function increaseFont() {
    console.log("increaseFont")
}

function decreaseFont() {
    console.log("decreaseFont")
}