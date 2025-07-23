const win = window as any;
export const languages = {
    "Common": {},
    "Spaceflight": {},
    "ChristmasCrash": {}
};

if (!win.languages) {
    win.languages = {};
}

win.languages.zh_cn = languages;