import { db } from './db';
import { starterNotes } from './content';
import {fullCaseBody} from './case-content';
import library from '@/content/library.json';
export type Post={id:string;slug:string;title:string;summary:string;content:string;type:string;tags:string[];published:boolean;published_at:string|null;updated_at?:string|null;seo_description:string;cover_url:string|null};
export async function publicPosts():Promise<Post[]>{
 if(process.env.DATABASE_URL){const {rows}=await db().query('SELECT * FROM posts WHERE published = true AND published_at <= NOW() ORDER BY published_at DESC');return rows}
 const starters=starterNotes.map((p,i)=>({id:`starter-${i}`,slug:p.slug,title:p.title,summary:p.summary,content:fullCaseBody(p.slug)||p.body,type:p.type,tags:[p.tag],published:true,published_at:null,seo_description:p.summary,cover_url:null}));
 const articles=library.map((p,i)=>({id:`library-${i}`,slug:p.slug,title:p.title,summary:p.summary,content:p.content,type:p.type,tags:p.tags,published:true,published_at:'2026-10-14T00:00:00.000Z',seo_description:p.seo_description,cover_url:null}));
 return [...starters,...articles];
}
export async function postBySlug(slug:string):Promise<Post|undefined>{if(process.env.DATABASE_URL){return (await db().query('SELECT * FROM posts WHERE slug=$1 AND published=true AND published_at <= NOW()',[slug])).rows[0]}return (await publicPosts()).find(p=>p.slug===slug)}
