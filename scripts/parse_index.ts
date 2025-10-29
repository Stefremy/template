import * as fs from 'fs';
import * as path from 'path';

// Path to index.html
const indexPath = path.join(__dirname, '../nordicus/index.html');

try {
  const data = fs.readFileSync(indexPath, 'utf-8');
  console.log('index.html contents:');
  console.log(data);
} catch (err) {
  console.error('Error reading index.html:', err);
}