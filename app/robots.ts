import {siteBase} from '@/lib/seo';export default function robots(){return {rules:{userAgent:'*',allow:['/','/api/og','/api/media/'],disallow:['/admin','/api/']},sitemap:`${siteBase()}/sitemap.xml`}}
