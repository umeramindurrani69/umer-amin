import { marked } from 'marked';
import sanitize from 'sanitize-html';
export function renderMarkdown(content:string){let index=0;return sanitize(marked.parse(content,{async:false}) as string,{allowedTags:sanitize.defaults.allowedTags.concat(['img']),allowedAttributes:{a:['href','title'],img:['src','alt','width','height']},allowedSchemes:['http','https','mailto']}).replace(/<h([23])>(.*?)<\/h\1>/g,(_,level,text)=>`<h${level} id="section-${++index}">${text}</h${level}>`)}
export function articleOutline(html:string){return [...html.matchAll(/<h[23] id="(section-\d+)">(.*?)<\/h[23]>/g)].map(m=>({id:m[1],title:m[2].replace(/<[^>]*>/g,'')}))}
