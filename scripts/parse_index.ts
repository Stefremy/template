import * as fs from 'fs';
import * as path from 'path';

// Path to linke/index resolved relative to repo root
const repoRoot = path.resolve(__dirname, '..');
const IN_PATH = path.resolve(repoRoot, 'linke', 'index');

try {
  const data = fs.readFileSync(IN_PATH, 'utf-8');
  console.log('index contents:');
  console.log(data);
} catch (err) {
  console.error('Error reading index:', err);
}