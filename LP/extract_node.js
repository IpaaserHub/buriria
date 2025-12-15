
const fs = require('fs');
const path = require('path');

const xmlPath = path.join('temp_docx', 'word', 'document.xml');
const keyXmlPath = path.join('temp_docx', 'word', 'document.xml');

if (!fs.existsSync(xmlPath)) {
    console.error("XML file not found:", xmlPath);
    process.exit(1);
}

const xmlContent = fs.readFileSync(xmlPath, 'utf8');

// Simple regex to extract text from <w:t> tags
const regex = /<w:t[^>]*>(.*?)<\/w:t>/g;
let match;
let extractedText = "";

// Also handle paragraph breaks <w:p> to add newlines?
// Actually, let's just grab all <w:p> and then inner <w:t>
// Better: split by <w:p>, then join inner <w:t>
const pRegex = /<w:p[\s\S]*?<\/w:p>/g;
const tRegex = /<w:t[^>]*>(.*?)<\/w:t>/g;

const paras = xmlContent.match(pRegex);

if (paras) {
    paras.forEach(p => {
        let pText = "";
        let tMatch;
        while ((tMatch = tRegex.exec(p)) !== null) {
            pText += tMatch[1];
        }
        if (pText) {
            extractedText += pText + "\n";
        }
    });
} else {
    // Fallback if structure is weird
    while ((match = regex.exec(xmlContent)) !== null) {
        extractedText += match[1];
    }
}

fs.writeFileSync('extracted_content.txt', extractedText, 'utf8');
console.log("Extraction complete.");
