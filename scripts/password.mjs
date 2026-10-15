import { passwordHash } from '../lib/security.mjs';
import { createInterface } from 'node:readline/promises';
const io=createInterface({input:process.stdin,output:process.stdout});
const password=await io.question('Choose an admin password (input is visible locally): ');
if(password.length<12)throw new Error('Use at least 12 characters.');
console.log('ADMIN_PASSWORD_HASH='+passwordHash(password));io.close();
