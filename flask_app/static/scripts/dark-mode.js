// The purpose of this file is to allow the user to switch between light and dark themes.

const themePrimaryLight = 'var(--bs-light)';
const themeContrastLight = 'var(--bs-dark)';

const themePrimaryDark = 'var(--bs-dark)';
const themeContrastDark = 'var(--bs-light)';

const themeSwitch = document.getElementById('themeSwitch');
const themeSwitchLabel = document.getElementById('themeSwitchLabel');

// If set to true, dark mode is enabled.
function updateTheme() {
    let root = document.querySelector(':root');

    let darkModeEnabled = localStorage.getItem('darkMode') === 'true';

    if (themeSwitch && themeSwitchLabel) {
        themeSwitch.checked = darkModeEnabled;
        themeSwitchLabel.textContent = darkModeEnabled ? 'Dark Mode' : 'Light Mode';
    }

    document.querySelector(':root').style.setProperty('--primary-color', darkModeEnabled ? themePrimaryDark : themePrimaryLight);
    document.querySelector(':root').style.setProperty('--contrast-color', darkModeEnabled ? themeContrastDark : themeContrastLight);
};

if (themeSwitch) {
    themeSwitch.addEventListener('change', function() {
        let darkModeEnabled = themeSwitch.checked;
        localStorage.setItem('darkMode', darkModeEnabled);

        updateTheme();
    });
}

document.addEventListener('DOMContentLoaded', function() {
    updateTheme();
});