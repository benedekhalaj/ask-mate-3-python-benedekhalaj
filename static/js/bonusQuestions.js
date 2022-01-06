// you receive an array of objects which you must sort in the by the key "sortField" in the "sortDirection"
function getSortedItems(items, sortField, sortDirection) {
    let numberFields = ['VoteCount', 'ViewNumber']

    if (sortDirection === "asc") {
        if (numberFields.includes(sortField)) {
            items.sort((a, b) => a[sortField] - b[sortField])
        }
        else {
            items.sort((a, b) => a[sortField] > b[sortField])
        }
    }
    else {
        if (numberFields.includes(sortField)) {
            items.sort((a, b) => b[sortField] - a[sortField])
        }
        else {
            items.sort((a, b) => a[sortField] < b[sortField])
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
    let themeButton = document.getElementById('theme-button');
    let bonusQuestions = document.getElementById('bonus-questions');
    if (bonusQuestions.style.color === 'black') {
        bonusQuestions.style.transition = 'ease 0.5s';
        bonusQuestions.style.backgroundColor = '#1c8fa6';
        bonusQuestions.style.color = 'white';
        themeButton.innerText = 'Change Theme to Light';
    }
    else {
        bonusQuestions.style.transition = 'ease 0.5s';
        bonusQuestions.style.backgroundColor = 'white';
        bonusQuestions.style.color = 'black';
        themeButton.innerText = 'Change Theme to Dark';
    }

}

function increaseFont() {
    let bonusQuestions = document.getElementById('bonus-questions');
    if (+bonusQuestions.style.fontSize.slice(0, -2) < 15) {
        bonusQuestions.style.fontSize = +bonusQuestions.style.fontSize.slice(0, -2) + 1;
    }

}

function decreaseFont() {
    let bonusQuestions = document.getElementById('bonus-questions');
    if (+bonusQuestions.style.fontSize.slice(0, -2) > 3) {
        bonusQuestions.style.fontSize = +bonusQuestions.style.fontSize.slice(0, -2) - 1;
    }
}