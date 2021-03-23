# Micro CMS v1

## Flags

### Flag0

When you access the page number 5 (/page/5), you receive a HTTP 403 code. You can access the page via edit (/page/edit/5). The body contains the flag.

### Flag1

SQL Injection by closing the WHERE close with `'` : `/page/edit/'`

### Flag2

While editing a page insert a javascript button in the **body** of a page `<button onclick="(function(){ alert(this);})()" >Some button</button>`, then save and inpect the button html code. The button contains a flag property.

### Flag3

While editing a page insert a javascript button in the **title** of a page `<button onclick="(function(){ alert(this);})()" >Some button</button>`, then save and go back to home. You will be greeted by a javascript pop-up containing the flag.