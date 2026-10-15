import { Pool } from 'pg';
import nextEnv from '@next/env';
nextEnv.loadEnvConfig(process.cwd());
if(!process.env.DATABASE_URL) throw new Error('Set DATABASE_URL in .env.local first.');
const pool=new Pool({connectionString:process.env.DATABASE_URL});
await pool.query(`CREATE TABLE IF NOT EXISTS posts(id UUID PRIMARY KEY DEFAULT gen_random_uuid(),slug TEXT UNIQUE NOT NULL,title TEXT NOT NULL,summary TEXT NOT NULL DEFAULT '',content TEXT NOT NULL DEFAULT '',type TEXT NOT NULL DEFAULT 'Field note',tags TEXT[] NOT NULL DEFAULT '{}',published BOOLEAN NOT NULL DEFAULT false,published_at TIMESTAMPTZ,seo_description TEXT NOT NULL DEFAULT '',cover_url TEXT,created_at TIMESTAMPTZ NOT NULL DEFAULT NOW(),updated_at TIMESTAMPTZ NOT NULL DEFAULT NOW()); CREATE INDEX IF NOT EXISTS posts_published_idx ON posts(published,published_at DESC)`);
await pool.end();console.log('Portfolio posts table ready.');
