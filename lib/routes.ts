export const isCaseStudy=(type:string)=>type==='Case study';
export const postPath=(post:{type:string;slug:string})=>`${isCaseStudy(post.type)?'/case-studies':'/research'}/${post.slug}`;
