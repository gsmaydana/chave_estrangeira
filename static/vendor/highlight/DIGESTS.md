## Subresource Integrity

If you are loading Highlight.js via CDN you may wish to use [Subresource Integrity](https://developer.mozilla.org/en-US/docs/Web/Security/Subresource_Integrity) to guarantee that you are using a legimitate build of the library.

To do this you simply need to add the `integrity` attribute for each JavaScript file you download via CDN. These digests are used by the browser to confirm the files downloaded have not been modified.

```html
<script
  src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.10.0/highlight.min.js"
  integrity="sha384-pGqTJHE/m20W4oDrfxTVzOutpMhjK3uP/0lReY0Jq/KInpuJSXUnk4WAYbciCLqT"></script>
<!-- including any other grammars you might need to load -->
<script
  src="//cdnjs.cloudflare.com/ajax/libs/highlight.js/11.10.0/languages/go.min.js"
  integrity="sha384-Mtb4EH3R9NMDME1sPQALOYR8KGqwrXAtmc6XGxDd0XaXB23irPKsuET0JjZt5utI"></script>
```

The full list of digests for every file can be found below.

### Digests

```
sha384-no5/zgQGupzPFGWV8VpJzfQau5/GI2v5b7I45l6nKc8gMOxzBHfgyxNdjQEnmW94 /es/languages/bash.js
sha384-u2nRnIxVxHkjnpxFScw/XgxNVuLz4dXXiT56xbp+Kk2b8AuStNgggHNpM9HO569A /es/languages/bash.min.js
sha384-+9dzNYaLHp3OPspFCOJGrEwfiOV3yqeD/atUDYVt9zKUJ8IW2QxffCT2LfmGfwfW /es/languages/css.js
sha384-G44u1/pUATC8754FIKYqkCxCl9AQYnspnFxzuR3RB1YVnTvqOEofqvZNQMUWcY/1 /es/languages/css.min.js
sha384-dpaRAfrfqLJ/m4qzPviZ8UztzpU27eoBSH+8GjP1nkccMBZ6x9EnnhvlNYMDz0P2 /es/languages/django.js
sha384-xmWxMjSXleWbbNXqoQdpI8OkRJnRmiuJ8cmkovyFJSZxyjycv8DA4XuENvWPDLDk /es/languages/django.min.js
sha384-oQpcUGMBf+VDTHOLQ1uhPp1FgNBo0OZc9gbXGuVFwAogHlkh/Iw6cvKKgcgCQkmV /es/languages/javascript.js
sha384-3T8DJ91yCa1//uY9h8Bo4QLrgEtbz4ILN2x9kSM4QWX9/1kKu6UXC3RAbVQV85UQ /es/languages/javascript.min.js
sha384-R87hRh4kF8+iz2sB6FvLrfR0XZBohjFXeJKIXld1Eji2UVi+M2+OIgJKma/9Ko6u /es/languages/json.js
sha384-QFDPNpqtrgZCuAr70TZJFM4VCY+xNnyGKwJw2EsWIBJOVcWAns9PHcLzecyDVv+x /es/languages/json.min.js
sha384-WuxmFqZ8YXr3xyK1Salq5t1q46F/VyzVGx48M2ZJPhbodzQ9L8kfnP/0seU78NsC /es/languages/nginx.js
sha384-XOua+gbAwDawIeMkI2pkXOZH9Xxl9/XLoGuPJD5Bs3WS4bMn207o20s+aQtpsqqE /es/languages/nginx.min.js
sha384-+ORCyjxlNVWQ/xCTFlWWc05iwK/J1wTnRy61YcExQSzVjhYQj3DPGtydA9IB3KQy /es/languages/pgsql.js
sha384-OH8IAQNE+/4/z6sdDTBio6BftdgqOsadsVYkSooVoUwdZYg95qly80XMjUigH5zk /es/languages/pgsql.min.js
sha384-e+d8RFZbtc5Pmt3xfX9uuElm63v5qOj7T5hAkkFbnYc1wEk7wCLlzOsm66MCf5Uk /es/languages/python.js
sha384-CPHh+9FxkWF3OtMZdTj5oQN1Qti0p4/5XBABz/JdgssOKHmfAOFz6Gu4tsG6MQiH /es/languages/python.min.js
sha384-ZX3mm6sjLYWMBTMUJYzvQXYHNWVJkD+t1ppx4BysyVs6cVhvYFVuwMlVCeAwtwm9 /es/languages/sql.js
sha384-DloKeCkj/pTPHeqWu3keGoEPpZJGm44yQjSmSfpWasykAMUobM0hcYFFPsg1PE6K /es/languages/sql.min.js
sha384-4SbTAv3AX2fuPCpSv6HW3p07YgA7hFfcwG2zJHtYv0ATIt1juD3IXj2NSYwTeIpm /languages/bash.js
sha384-83HvQQdGTWqnRLmgm19NjCb1+/awKJGytUX9sm3HJb2ddZ9Fs1Bst2bZogFjt9rr /languages/bash.min.js
sha384-h6xPJgkyvp13tIs697wZHjCH20tW1aJOrvnAKiZZiATSWZp0lyLB4bAdsEhWUSze /languages/css.js
sha384-+MO3D3y/aZzZq7QMAAA5KiuAcqBZivJHFmVUXfwdBoLxEXeGTeQGsNMll4fpnegg /languages/css.min.js
sha384-gfyiMmAn2+1KPBU6zgf5/GuxwAS1MG2sXO2QNIa1b8gWqS+ZAEGASFZUv2DTTr0I /languages/django.js
sha384-E8a05vTFeTlJrGsYy6uvHSN7YyYtYVDfuTB0NYKryrTqkKAh0Kljndtou/5x9KxE /languages/django.min.js
sha384-p/utwvqrRVOLlz0BjJ0BCGCb2liTDipfz47/QmGXz9hoPIjCKYEgmYUC30VmGgZy /languages/javascript.js
sha384-L/XmDiyusXomLRGcRmcBpPlboRFjpQNV747OJvg+sEOpgGYvUsNwcC4JLNQ2dI6O /languages/javascript.min.js
sha384-psmmPlbfEWGyvRapexDqkVTgNz7Y1xvlGdLNWQSafI4GFQYFDXPZxVXH1laU4n6l /languages/json.js
sha384-Bb6DhE3tUpBROwypL78TbhRUs9QbCt2GxcxVSYglt2l3MefrYkm4CfwjfWhRfQaX /languages/json.min.js
sha384-GqxuhQ5X9X3c8nNswtucj7gX9fAuYCtI73NbFLXAYNqX39+zocekxv7SOK6oVGhi /languages/nginx.js
sha384-TG8jUbt29ktiHxVaCkA6FLnJkL/PYG3zQwEYexdbr+Z6mMkFf+c0ONpHyuIY4vvG /languages/nginx.min.js
sha384-QYdE/O+kYLzPISnj43XU2PBSQGgHxlNW3s9e1CfQn3/mdj2U2lygqPmCk6mh24Ib /languages/pgsql.js
sha384-oJqzx2KYttoB62Br3yGkuDMB7q08+JIjBH1jiTmGfz94kIjSpP8WFYdneQESWp3z /languages/pgsql.min.js
sha384-WNah6F2QDUbmrNCi0fSEyKJbSb01S1ijnoiwbDnegW7dm2Cz/H1CiH1HhWlUvj01 /languages/python.js
sha384-YDj7s2Wf0QEwarV3OB8lvoNJJCH032vOLMDo2HDrYiEpQ+QmKN+e++x3hElX5S+w /languages/python.min.js
sha384-w/OmtgUvmlKWaVatpcvuEQxP7bkJzI5gLeeQkuXjApJNiQvNmXFL2PBM5RWgKqDr /languages/sql.js
sha384-2uzCjI3OPwJce6i2hphsYs1qqTqRrDnfPXbfjZggPWy2/Lgl8gzV9Hyl0jhhoWy4 /languages/sql.min.js
sha384-iO17CdMk5SY3iyr8Zk4nCLFppADA6R6ERkp8wy49QvsGcnpJ2Mnq4/olKaitkei6 /highlight.js
sha384-oiruX/xhpUsq32pVXLD6hHxM+4wHxByRnDP4hFgeFHKneR9gZ4EMdwSJybBuEWu0 /highlight.min.js
```

