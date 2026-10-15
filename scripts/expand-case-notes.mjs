import ts from 'typescript';import {readFileSync} from 'node:fs';import {Pool} from 'pg';import nextEnv from '@next/env';nextEnv.loadEnvConfig(process.cwd());
const content=ts.transpileModule(readFileSync('lib/content.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext}}).outputText;
const contentUrl='data:text/javascript;base64,'+Buffer.from(content).toString('base64');
let cases=ts.transpileModule(readFileSync('lib/case-content.ts','utf8'),{compilerOptions:{module:ts.ModuleKind.ESNext}}).outputText.replace("'./content'",JSON.stringify(contentUrl));
const {starterNotes}=await import(contentUrl);const {fullCaseBody}=await import('data:text/javascript;base64,'+Buffer.from(cases).toString('base64'));const pool=new Pool({connectionString:process.env.DATABASE_URL});
let count=0;for(const n of starterNotes){const expanded=fullCaseBody(n.slug);if(expanded)count+=(await pool.query('UPDATE posts SET content=$1,updated_at=NOW() WHERE slug=$2 AND content=$3',[expanded,n.slug,n.body])).rowCount}
await pool.end();console.log(`${count} unchanged introductory case studies expanded. Other posts preserved.`);
