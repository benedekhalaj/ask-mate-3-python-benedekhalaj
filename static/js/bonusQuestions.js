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
    for (let item of items) {
        if (filterValue[0] === '!') {
            if (filterValue.includes(':')) {
                let [tag, value] = filterValue.split(':');
                if (!item[tag.slice(1, tag.length)].includes(value)) {
                    filteredItems.push(item)
                }
            }
            else if (Object.values(item).every((string) => valueNotInAnyString(string, filterValue))) {
                filteredItems.push(item);
            }
        }
        else {
            if (filterValue.includes(':')) {
                let [tag, value] = filterValue.split(':');
                if (item[tag].includes(value)) {
                    filteredItems.push(item)
                }
            }
            else {
                if (Object.values(item).some((string) => valueInAnyString(string, filterValue))) {
                filteredItems.push(item);
                }
            }

        }
    }
    return filteredItems
}

function valueInAnyString(string, value) {
    return string.includes(value)
}

function valueNotInAnyString(string, value) {
    return !string.includes(value.slice(1, value.length))
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
