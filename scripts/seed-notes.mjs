import {Pool} from 'pg';import nextEnv from '@next/env';import ts from 'typescript';import {readFileSync} from 'node:fs';
const source=ts.transpileModule(readFileSync(new URL('../lib/content.ts',import.meta.url),'utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext}}).outputText;
const {starterNotes}=await import('data:text/javascript;base64,'+Buffer.from(source).toString('base64'));
nextEnv.loadEnvConfig(process.cwd());
const p=new Pool({connectionString:process.env.DATABASE_URL});
for(const n of starterNotes)await p.query('INSERT INTO posts(slug,title,summary,content,type,tags,published,published_at,seo_description) VALUES($1,$2,$3,$4,$5,$6,true,NOW(),$3) ON CONFLICT(slug) DO NOTHING',[n.slug,n.title,n.summary,n.body,n.type,[n.tag]]);
await p.end();console.log('Three introductory project notes added. Existing posts preserved.');
