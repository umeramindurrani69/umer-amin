import { cookies } from 'next/headers';import {siteBase} from './seo';
import { validSession } from './security.mjs';
export const configured=()=>Boolean(process.env.ADMIN_EMAIL&&process.env.ADMIN_PASSWORD_HASH&&process.env.SESSION_SECRET&&process.env.SESSION_SECRET.length>=32);
export async function isAdmin(){return configured()&&validSession((await cookies()).get('portfolio_session')?.value,process.env.SESSION_SECRET)}
export function sameOrigin(req:Request){const origin=req.headers.get('origin');const expected=process.env.SITE_URL||(process.env.VERCEL?siteBase():new URL(req.url).origin);return origin===new URL(expected).origin}
