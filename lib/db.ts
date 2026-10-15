import { Pool } from 'pg';
const globalDb=globalThis as unknown as { portfolioPool?: Pool };
export function db(){
 if(!process.env.DATABASE_URL) throw new Error('DATABASE_URL is not configured');
 return globalDb.portfolioPool ??= new Pool({connectionString:process.env.DATABASE_URL,max:5,connectionTimeoutMillis:3000});
}
export async function dbReady(){try{await db().query('SELECT id FROM posts LIMIT 1');return true}catch{return false}}
