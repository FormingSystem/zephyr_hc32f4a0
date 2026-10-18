---
id: learning.zephyr-docs.api-fota-storage-topic-reference.page-4
title: HTTP响应状态码（Response Status Codes）。
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/group__http__status__codes.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_HTTP响应状态码（Response Status Codes）。

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/group__http__status__codes.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

HTTP响应状态码（Response Status Codes）。

<a id="details"></a>

HTTP 响应状态码（HTTP Response Status Codes）。自（Since）3.3 起提供，版本（Version）0.8.0。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 4.1\_枚举（Enumerations）

<a id="r_gabc3b93f68c8bdd857ad32913628dfa8d"></a>

```c
enum http_status { HTTP_100_CONTINUE = 100 , HTTP_101_SWITCHING_PROTOCOLS = 101 , HTTP_102_PROCESSING = 102 , HTTP_103_EARLY_HINTS = 103 , HTTP_200_OK = 200 , HTTP_201_CREATED = 201 , HTTP_202_ACCEPTED = 202 , HTTP_203_NON_AUTHORITATIVE_INFORMATION = 203 , HTTP_204_NO_CONTENT = 204 , HTTP_205_RESET_CONTENT = 205 , HTTP_206_PARTIAL_CONTENT = 206 , HTTP_207_MULTI_STATUS = 207 , HTTP_208_ALREADY_REPORTED = 208 , HTTP_226_IM_USED = 226 , HTTP_300_MULTIPLE_CHOICES = 300 , HTTP_301_MOVED_PERMANENTLY = 301 , HTTP_302_FOUND = 302 , HTTP_303_SEE_OTHER = 303 , HTTP_304_NOT_MODIFIED = 304 , HTTP_305_USE_PROXY = 305 , HTTP_306_UNUSED = 306 , HTTP_307_TEMPORARY_REDIRECT = 307 , HTTP_308_PERMANENT_REDIRECT = 308 , HTTP_400_BAD_REQUEST = 400 , HTTP_401_UNAUTHORIZED = 401 , HTTP_402_PAYMENT_REQUIRED = 402 , HTTP_403_FORBIDDEN = 403 , HTTP_404_NOT_FOUND = 404 , HTTP_405_METHOD_NOT_ALLOWED = 405 , HTTP_406_NOT_ACCEPTABLE = 406 , HTTP_407_PROXY_AUTHENTICATION_REQUIRED = 407 , HTTP_408_REQUEST_TIMEOUT = 408 , HTTP_409_CONFLICT = 409 , HTTP_410_GONE = 410 , HTTP_411_LENGTH_REQUIRED = 411 , HTTP_412_PRECONDITION_FAILED = 412 , HTTP_413_PAYLOAD_TOO_LARGE = 413 , HTTP_414_URI_TOO_LONG = 414 , HTTP_415_UNSUPPORTED_MEDIA_TYPE = 415 , HTTP_416_RANGE_NOT_SATISFIABLE = 416 , HTTP_417_EXPECTATION_FAILED = 417 , HTTP_418_IM_A_TEAPOT = 418 , HTTP_421_MISDIRECTED_REQUEST = 421 , HTTP_422_UNPROCESSABLE_ENTITY = 422 , HTTP_423_LOCKED = 423 , HTTP_424_FAILED_DEPENDENCY = 424 , HTTP_425_TOO_EARLY = 425 , HTTP_426_UPGRADE_REQUIRED = 426 , HTTP_428_PRECONDITION_REQUIRED = 428 , HTTP_429_TOO_MANY_REQUESTS = 429 , HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE = 431 , HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS = 451 , HTTP_500_INTERNAL_SERVER_ERROR = 500 , HTTP_501_NOT_IMPLEMENTED = 501 , HTTP_502_BAD_GATEWAY = 502 , HTTP_503_SERVICE_UNAVAILABLE = 503 , HTTP_504_GATEWAY_TIMEOUT = 504 , HTTP_505_HTTP_VERSION_NOT_SUPPORTED = 505 , HTTP_506_VARIANT_ALSO_NEGOTIATES = 506 , HTTP_507_INSUFFICIENT_STORAGE = 507 , HTTP_508_LOOP_DETECTED = 508 , HTTP_510_NOT_EXTENDED = 510 , HTTP_511_NETWORK_AUTHENTICATION_REQUIRED = 511 }
```

相关声明：[http_status](#gabc3b93f68c8bdd857ad32913628dfa8d)、[HTTP_100_CONTINUE](#ggabc3b93f68c8bdd857ad32913628dfa8dacd840de9c8d9601982b1e13f9d00e882)、[HTTP_101_SWITCHING_PROTOCOLS](#ggabc3b93f68c8bdd857ad32913628dfa8da8663a5f332b7837c96599b127c2616d5)、[HTTP_102_PROCESSING](#ggabc3b93f68c8bdd857ad32913628dfa8da365b2bd5e2ea86fa9e95e219a11ae0af)、[HTTP_103_EARLY_HINTS](#ggabc3b93f68c8bdd857ad32913628dfa8dab51c1485692490f10f115323192655f0)、[HTTP_200_OK](#ggabc3b93f68c8bdd857ad32913628dfa8da95005af4e6e4478af07e395d5b40fca9)、[HTTP_201_CREATED](#ggabc3b93f68c8bdd857ad32913628dfa8da049723ca514a8a4383d37d341389671a)、[HTTP_202_ACCEPTED](#ggabc3b93f68c8bdd857ad32913628dfa8da8876c5cb07aab2c49b60f8162c55c2a9)、[HTTP_203_NON_AUTHORITATIVE_INFORMATION](#ggabc3b93f68c8bdd857ad32913628dfa8da2a9336f89d5ec5a75ee507456bd126ce)、[HTTP_204_NO_CONTENT](#ggabc3b93f68c8bdd857ad32913628dfa8da663e0e9bb7aabc67d94c9e21fd498b93)、[HTTP_205_RESET_CONTENT](#ggabc3b93f68c8bdd857ad32913628dfa8daebf6ddfe7266b27a8c1463b213274255)、[HTTP_206_PARTIAL_CONTENT](#ggabc3b93f68c8bdd857ad32913628dfa8da8cf9268deed8f7326477cc9ca75c56b2)、[HTTP_207_MULTI_STATUS](#ggabc3b93f68c8bdd857ad32913628dfa8da19dd55c06c6f613ab8c3d0cf62a60e7d)、[HTTP_208_ALREADY_REPORTED](#ggabc3b93f68c8bdd857ad32913628dfa8daac56bbd7352cd0aa7482bf18f03dd47f)、[HTTP_226_IM_USED](#ggabc3b93f68c8bdd857ad32913628dfa8da92cbf60d86ad7cfc37dffea8fac8284b)、[HTTP_300_MULTIPLE_CHOICES](#ggabc3b93f68c8bdd857ad32913628dfa8dabbcf6453c3f7487f405f6434decf4435)、[HTTP_301_MOVED_PERMANENTLY](#ggabc3b93f68c8bdd857ad32913628dfa8daa1233081760e3a200b40a803d90a838f)、[HTTP_302_FOUND](#ggabc3b93f68c8bdd857ad32913628dfa8dab6b1056e30f4f934f47a17cd5d9978dc)、[HTTP_303_SEE_OTHER](#ggabc3b93f68c8bdd857ad32913628dfa8dace9856b68ab35f424af83d10ae41ec51)、[HTTP_304_NOT_MODIFIED](#ggabc3b93f68c8bdd857ad32913628dfa8da8b9f56ce4e7b089e925d1ed8dce37bf8)、[HTTP_305_USE_PROXY](#ggabc3b93f68c8bdd857ad32913628dfa8da17cded8509d8f2d127c10755e96c45aa)、[HTTP_306_UNUSED](#ggabc3b93f68c8bdd857ad32913628dfa8da90d6cc67e4d7c7af04bf01669bb9a981)、[HTTP_307_TEMPORARY_REDIRECT](#ggabc3b93f68c8bdd857ad32913628dfa8da38136e534754d25b92dfeeec7822acf7)、[HTTP_308_PERMANENT_REDIRECT](#ggabc3b93f68c8bdd857ad32913628dfa8da41a528c645fc6033b03c9e3586413416)、[HTTP_400_BAD_REQUEST](#ggabc3b93f68c8bdd857ad32913628dfa8da573e52d342de96715fafca473db9e63c)、[HTTP_401_UNAUTHORIZED](#ggabc3b93f68c8bdd857ad32913628dfa8daec7448b9f31b792930fa812529fdb113)、[HTTP_402_PAYMENT_REQUIRED](#ggabc3b93f68c8bdd857ad32913628dfa8daf3b35487d12f9c68cac8dfb18258fd3b)、[HTTP_403_FORBIDDEN](#ggabc3b93f68c8bdd857ad32913628dfa8da01a39dead7f1e06819788111cf091d00)、[HTTP_404_NOT_FOUND](#ggabc3b93f68c8bdd857ad32913628dfa8daa7daeb030bdc63080a76316ea49d7875)、[HTTP_405_METHOD_NOT_ALLOWED](#ggabc3b93f68c8bdd857ad32913628dfa8da90c5df830e4a4870d159568ab467a163)、[HTTP_406_NOT_ACCEPTABLE](#ggabc3b93f68c8bdd857ad32913628dfa8da12683b2ef168145ba3ea15fdcfa5a3d0)、[HTTP_407_PROXY_AUTHENTICATION_REQUIRED](#ggabc3b93f68c8bdd857ad32913628dfa8dac8ab478cacfd4a65de54a89aa624d4e4)、[HTTP_408_REQUEST_TIMEOUT](#ggabc3b93f68c8bdd857ad32913628dfa8da2dcdac23926991c19e356591f445cc01)、[HTTP_409_CONFLICT](#ggabc3b93f68c8bdd857ad32913628dfa8da1f9f47f3f238245eb929593d97b08c50)、[HTTP_410_GONE](#ggabc3b93f68c8bdd857ad32913628dfa8da7e1ed57551254aa0c1ac6bfc3379e444)、[HTTP_411_LENGTH_REQUIRED](#ggabc3b93f68c8bdd857ad32913628dfa8dadde89da537b429fc18b290eafba0bd93)、[HTTP_412_PRECONDITION_FAILED](#ggabc3b93f68c8bdd857ad32913628dfa8da41054511d912380bf3e8f8a5fc6481f5)、[HTTP_413_PAYLOAD_TOO_LARGE](#ggabc3b93f68c8bdd857ad32913628dfa8da24bbe6f0c14303e45f3bed4fd5abda35)、[HTTP_414_URI_TOO_LONG](#ggabc3b93f68c8bdd857ad32913628dfa8dadc6ba425c30238e9d77c250ee0666807)、[HTTP_415_UNSUPPORTED_MEDIA_TYPE](#ggabc3b93f68c8bdd857ad32913628dfa8dadc804c5b375895e6097567b092041abd)、[HTTP_416_RANGE_NOT_SATISFIABLE](#ggabc3b93f68c8bdd857ad32913628dfa8da64e4af58b6c32a5bc230d219ef169095)、[HTTP_417_EXPECTATION_FAILED](#ggabc3b93f68c8bdd857ad32913628dfa8dab672f6b0001fe4913b0bec2e1d894eae)、[HTTP_418_IM_A_TEAPOT](#ggabc3b93f68c8bdd857ad32913628dfa8da5e0e4a0d3b729bb824109850cc835762)、[HTTP_421_MISDIRECTED_REQUEST](#ggabc3b93f68c8bdd857ad32913628dfa8da9c09b98973f0587bd40a8799d9b9327b)、[HTTP_422_UNPROCESSABLE_ENTITY](#ggabc3b93f68c8bdd857ad32913628dfa8da64c040b238b1fafb97064e94e022e8b8)、[HTTP_423_LOCKED](#ggabc3b93f68c8bdd857ad32913628dfa8da0b4980ea5622d3bb6ff4f3cbd35019d7)、[HTTP_424_FAILED_DEPENDENCY](#ggabc3b93f68c8bdd857ad32913628dfa8da158e8935ffa9feeb34872894b2bbb9a3)、[HTTP_425_TOO_EARLY](#ggabc3b93f68c8bdd857ad32913628dfa8dac36e0befced387ab34536b913bc5fdfc)、[HTTP_426_UPGRADE_REQUIRED](#ggabc3b93f68c8bdd857ad32913628dfa8da54937864193a60117b3292a648e32fb2)、[HTTP_428_PRECONDITION_REQUIRED](#ggabc3b93f68c8bdd857ad32913628dfa8dab90a0098eaf6d21537624059b281ad98)、[HTTP_429_TOO_MANY_REQUESTS](#ggabc3b93f68c8bdd857ad32913628dfa8da8cb955695255e2ae409a3ae758a4785e)、[HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE](#ggabc3b93f68c8bdd857ad32913628dfa8da20dda0eafc4757992d73d82953074a14)、[HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS](#ggabc3b93f68c8bdd857ad32913628dfa8daf5c91a9d8a67f7dd9d794009f8afc8a1)、[HTTP_500_INTERNAL_SERVER_ERROR](#ggabc3b93f68c8bdd857ad32913628dfa8dade6299dbe0899702d3242f58c9a0f8e4)、[HTTP_501_NOT_IMPLEMENTED](#ggabc3b93f68c8bdd857ad32913628dfa8da6409f878aa7dc96869e51cefabe2f40b)、[HTTP_502_BAD_GATEWAY](#ggabc3b93f68c8bdd857ad32913628dfa8da38eeaf7c0b4bdc5dbe179db6ea734375)、[HTTP_503_SERVICE_UNAVAILABLE](#ggabc3b93f68c8bdd857ad32913628dfa8da8d7b1764f16f69d6631fcf971a5e3d5d)、[HTTP_504_GATEWAY_TIMEOUT](#ggabc3b93f68c8bdd857ad32913628dfa8da82f00cb61b88603756ed74061f88ab71)、[HTTP_505_HTTP_VERSION_NOT_SUPPORTED](#ggabc3b93f68c8bdd857ad32913628dfa8daa119343b9f0c57d39a587af025b63419)、[HTTP_506_VARIANT_ALSO_NEGOTIATES](#ggabc3b93f68c8bdd857ad32913628dfa8dab964d08c22b5a75583f9a999608b758e)、[HTTP_507_INSUFFICIENT_STORAGE](#ggabc3b93f68c8bdd857ad32913628dfa8dac52b5659581516f9c38bab6d33b26b97)、[HTTP_508_LOOP_DETECTED](#ggabc3b93f68c8bdd857ad32913628dfa8da9805a426667162c3429dc1c77cc1ab45)、[HTTP_510_NOT_EXTENDED](#ggabc3b93f68c8bdd857ad32913628dfa8da5296e8faf9e10e505d90a3c331cc1fbb)、[HTTP_511_NETWORK_AUTHENTICATION_REQUIRED](#ggabc3b93f68c8bdd857ad32913628dfa8dad9b064b230d0a39e262f5f2358d9c20a)。

HTTP响应状态码（Response Status Codes）。

## 4.2\_详细说明（Detailed Documentation）

<a id="gabc3b93f68c8bdd857ad32913628dfa8d"></a>

### `http_status`

```c
enum http_status
```

```c
#include <zephyr/net/http/status.h>
```

HTTP响应状态码（Response Status Codes）。

**枚举值（Enumerators）**

| 名称／方向 | 说明 |
| --- | --- |
| `HTTP_100_CONTINUE` | 继续（Continue）。 |
| `HTTP_101_SWITCHING_PROTOCOLS` | 切换协议（Switching Protocols）。 |
| `HTTP_102_PROCESSING` | 处理中（Processing）。 |
| `HTTP_103_EARLY_HINTS` | 提前提示（Early Hints）。 |
| `HTTP_200_OK` | 成功（OK）。 |
| `HTTP_201_CREATED` | 已创建（Created）。 |
| `HTTP_202_ACCEPTED` | 已接受（Accepted）。 |
| `HTTP_203_NON_AUTHORITATIVE_INFORMATION` | 非权威信息（Non-Authoritative Information）。 |
| `HTTP_204_NO_CONTENT` | 无内容（No Content）。 |
| `HTTP_205_RESET_CONTENT` | 重置内容（Reset Content）。 |
| `HTTP_206_PARTIAL_CONTENT` | 部分内容（Partial Content）。 |
| `HTTP_207_MULTI_STATUS` | 多状态（Multi-Status）。 |
| `HTTP_208_ALREADY_REPORTED` | 已报告（Already Reported）。 |
| `HTTP_226_IM_USED` | 已使用实例操作（IM Used）。 |
| `HTTP_300_MULTIPLE_CHOICES` | 多种选择（Multiple Choices）。 |
| `HTTP_301_MOVED_PERMANENTLY` | 永久移动（Moved Permanently）。 |
| `HTTP_302_FOUND` | 已找到（Found）。 |
| `HTTP_303_SEE_OTHER` | 查看其他资源（See Other）。 |
| `HTTP_304_NOT_MODIFIED` | 未修改（Not Modified）。 |
| `HTTP_305_USE_PROXY` | 使用代理（Use Proxy）。 |
| `HTTP_306_UNUSED` | 未使用（unused）。 |
| `HTTP_307_TEMPORARY_REDIRECT` | 临时重定向（Temporary Redirect）。 |
| `HTTP_308_PERMANENT_REDIRECT` | 永久重定向（Permanent Redirect）。 |
| `HTTP_400_BAD_REQUEST` | 错误请求（Bad Request）。 |
| `HTTP_401_UNAUTHORIZED` | 未经授权（Unauthorized）。 |
| `HTTP_402_PAYMENT_REQUIRED` | 需要付费（Payment Required）。 |
| `HTTP_403_FORBIDDEN` | 禁止（Forbidden）。 |
| `HTTP_404_NOT_FOUND` | 未找到（Not Found）。 |
| `HTTP_405_METHOD_NOT_ALLOWED` | 方法不允许（Method Not Allowed）。 |
| `HTTP_406_NOT_ACCEPTABLE` | 不可接受（Not Acceptable）。 |
| `HTTP_407_PROXY_AUTHENTICATION_REQUIRED` | 需要代理身份验证（Proxy Authentication Required）。 |
| `HTTP_408_REQUEST_TIMEOUT` | 请求超时（Request Timeout）。 |
| `HTTP_409_CONFLICT` | 冲突（Conflict）。 |
| `HTTP_410_GONE` | 资源已永久移除（Gone）。 |
| `HTTP_411_LENGTH_REQUIRED` | 需要长度（Length Required）。 |
| `HTTP_412_PRECONDITION_FAILED` | 前置条件失败（Precondition Failed）。 |
| `HTTP_413_PAYLOAD_TOO_LARGE` | 载荷过大（Payload Too Large）。 |
| `HTTP_414_URI_TOO_LONG` | URI 过长（URI Too Long）。 |
| `HTTP_415_UNSUPPORTED_MEDIA_TYPE` | 不支持的媒体类型（Unsupported Media Type）。 |
| `HTTP_416_RANGE_NOT_SATISFIABLE` | 无法满足范围请求（Range Not Satisfiable）。 |
| `HTTP_417_EXPECTATION_FAILED` | 预期条件失败（Expectation Failed）。 |
| `HTTP_418_IM_A_TEAPOT` | 我是茶壶（I'm a teapot）。 |
| `HTTP_421_MISDIRECTED_REQUEST` | 请求误导向（Misdirected Request）。 |
| `HTTP_422_UNPROCESSABLE_ENTITY` | 无法处理的实体（Unprocessable Entity）。 |
| `HTTP_423_LOCKED` | 已锁定（Locked）。 |
| `HTTP_424_FAILED_DEPENDENCY` | 依赖失败（Failed Dependency）。 |
| `HTTP_425_TOO_EARLY` | 过早（Too Early）。 |
| `HTTP_426_UPGRADE_REQUIRED` | 需要升级（Upgrade Required）。 |
| `HTTP_428_PRECONDITION_REQUIRED` | 需要前置条件（Precondition Required）。 |
| `HTTP_429_TOO_MANY_REQUESTS` | 请求过多（Too Many Requests）。 |
| `HTTP_431_REQUEST_HEADER_FIELDS_TOO_LARGE` | 请求首部字段过大（Request Header Fields Too Large）。 |
| `HTTP_451_UNAVAILABLE_FOR_LEGAL_REASONS` | 因法律原因不可用（Unavailable For Legal Reasons）。 |
| `HTTP_500_INTERNAL_SERVER_ERROR` | 服务器内部错误（Internal Server Error）。 |
| `HTTP_501_NOT_IMPLEMENTED` | 未实现（Not Implemented）。 |
| `HTTP_502_BAD_GATEWAY` | 网关错误（Bad Gateway）。 |
| `HTTP_503_SERVICE_UNAVAILABLE` | 服务不可用（Service Unavailable）。 |
| `HTTP_504_GATEWAY_TIMEOUT` | 网关超时（Gateway Timeout）。 |
| `HTTP_505_HTTP_VERSION_NOT_SUPPORTED` | 不支持的 HTTP 版本（HTTP Version Not Supported）。 |
| `HTTP_506_VARIANT_ALSO_NEGOTIATES` | 变体也参与协商（Variant Also Negotiates）。 |
| `HTTP_507_INSUFFICIENT_STORAGE` | 存储空间不足（Insufficient Storage）。 |
| `HTTP_508_LOOP_DETECTED` | 检测到循环（Loop Detected）。 |
| `HTTP_510_NOT_EXTENDED` | 未扩展（Not Extended）。 |
| `HTTP_511_NETWORK_AUTHENTICATION_REQUIRED` | 需要网络身份验证（Network Authentication Required）。 |

**说明（Note）**：注（Note）：HTTP 响应状态码须经 IANA 批准。

**参阅（See Also）**：另请参见（See also）：超文本传输协议状态码注册表（Hypertext Transfer Protocol (HTTP) Status Code Registry）、RFC 9110 HTTP 响应状态码（HTTP Response Status Codes）。


## 4.3\_原页交叉引用（Cross References）

- [zephyr/net/http/status.h](../api_file_reference/P406_zephyr__net__http__status.h_文件参考.md)
- [Hypertext Transfer Protocol (HTTP) Status Code Registry](https://www.iana.org/assignments/http-status-codes)
- [RFC 9110](https://datatracker.ietf.org/doc/html/rfc9110)
- [HTTP响应状态码（Response Status Codes）。](https://developer.mozilla.org/en-US/docs/Web/HTTP/Status)

<a id="header-details"></a>
<a id="doc-enum-members"></a>
<a id="header-doc-enum-members"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dacd840de9c8d9601982b1e13f9d00e882"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da8663a5f332b7837c96599b127c2616d5"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da365b2bd5e2ea86fa9e95e219a11ae0af"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dab51c1485692490f10f115323192655f0"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da95005af4e6e4478af07e395d5b40fca9"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da049723ca514a8a4383d37d341389671a"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da8876c5cb07aab2c49b60f8162c55c2a9"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da2a9336f89d5ec5a75ee507456bd126ce"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da663e0e9bb7aabc67d94c9e21fd498b93"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8daebf6ddfe7266b27a8c1463b213274255"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da8cf9268deed8f7326477cc9ca75c56b2"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da19dd55c06c6f613ab8c3d0cf62a60e7d"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8daac56bbd7352cd0aa7482bf18f03dd47f"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da92cbf60d86ad7cfc37dffea8fac8284b"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dabbcf6453c3f7487f405f6434decf4435"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8daa1233081760e3a200b40a803d90a838f"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dab6b1056e30f4f934f47a17cd5d9978dc"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dace9856b68ab35f424af83d10ae41ec51"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da8b9f56ce4e7b089e925d1ed8dce37bf8"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da17cded8509d8f2d127c10755e96c45aa"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da90d6cc67e4d7c7af04bf01669bb9a981"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da38136e534754d25b92dfeeec7822acf7"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da41a528c645fc6033b03c9e3586413416"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da573e52d342de96715fafca473db9e63c"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8daec7448b9f31b792930fa812529fdb113"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8daf3b35487d12f9c68cac8dfb18258fd3b"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da01a39dead7f1e06819788111cf091d00"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8daa7daeb030bdc63080a76316ea49d7875"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da90c5df830e4a4870d159568ab467a163"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da12683b2ef168145ba3ea15fdcfa5a3d0"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dac8ab478cacfd4a65de54a89aa624d4e4"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da2dcdac23926991c19e356591f445cc01"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da1f9f47f3f238245eb929593d97b08c50"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da7e1ed57551254aa0c1ac6bfc3379e444"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dadde89da537b429fc18b290eafba0bd93"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da41054511d912380bf3e8f8a5fc6481f5"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da24bbe6f0c14303e45f3bed4fd5abda35"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dadc6ba425c30238e9d77c250ee0666807"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dadc804c5b375895e6097567b092041abd"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da64e4af58b6c32a5bc230d219ef169095"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dab672f6b0001fe4913b0bec2e1d894eae"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da5e0e4a0d3b729bb824109850cc835762"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da9c09b98973f0587bd40a8799d9b9327b"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da64c040b238b1fafb97064e94e022e8b8"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da0b4980ea5622d3bb6ff4f3cbd35019d7"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da158e8935ffa9feeb34872894b2bbb9a3"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dac36e0befced387ab34536b913bc5fdfc"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da54937864193a60117b3292a648e32fb2"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dab90a0098eaf6d21537624059b281ad98"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da8cb955695255e2ae409a3ae758a4785e"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da20dda0eafc4757992d73d82953074a14"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8daf5c91a9d8a67f7dd9d794009f8afc8a1"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dade6299dbe0899702d3242f58c9a0f8e4"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da6409f878aa7dc96869e51cefabe2f40b"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da38eeaf7c0b4bdc5dbe179db6ea734375"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da8d7b1764f16f69d6631fcf971a5e3d5d"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da82f00cb61b88603756ed74061f88ab71"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8daa119343b9f0c57d39a587af025b63419"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dab964d08c22b5a75583f9a999608b758e"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dac52b5659581516f9c38bab6d33b26b97"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da9805a426667162c3429dc1c77cc1ab45"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8da5296e8faf9e10e505d90a3c331cc1fbb"></a>
<a id="ggabc3b93f68c8bdd857ad32913628dfa8dad9b064b230d0a39e262f5f2358d9c20a"></a>

---

[上一章](P003_基于 HTTP 的固件空中升级（FOTA HTTP）.md) · [返回大纲](大纲.md) · [下一章](P005_LSM6DSVXXX API主题.md)
