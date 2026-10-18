---
id: learning.zephyr-docs.api-source-reference.page-522
title: mgmt_defines.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mgmt__defines_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第522章\_mgmt\_defines.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/mgmt__defines_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/mgmt__defines_8h.html)。

## 522.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00010"></a>
<a id="l00011"></a>
<a id="l00012"></a>
<a id="l00013"></a>
<a id="l00014"></a>
<a id="l00015"></a>
<a id="l00016"></a>
<a id="l00021"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00034"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00038"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00042"></a>
<a id="l00043"></a>
<a id="l00044"></a>
<a id="foldopen00049"></a>
<a id="l00049"></a>
<a id="l00051"></a>
<a id="l00052"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00057"></a>
<a id="l00058"></a>
<a id="l00060"></a>
<a id="l00061"></a>
<a id="l00063"></a>
<a id="l00064"></a>
<a id="l00066"></a>
<a id="l00067"></a>
<a id="l00069"></a>
<a id="l00070"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00078"></a>
<a id="l00079"></a>
<a id="l00081"></a>
<a id="l00082"></a>
<a id="l00084"></a>
<a id="l00085"></a>
<a id="l00087"></a>
<a id="l00088"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="foldopen00099"></a>
<a id="l00099"></a>
<a id="l00101"></a>
<a id="l00102"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00110"></a>
<a id="l00111"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="l00116"></a>
<a id="l00117"></a>
<a id="l00119"></a>
<a id="l00120"></a>
<a id="l00122"></a>
<a id="l00123"></a>
<a id="l00125"></a>
<a id="l00126"></a>
<a id="l00128"></a>
<a id="l00129"></a>
<a id="l00131"></a>
<a id="l00132"></a>
<a id="l00134"></a>
<a id="l00135"></a>
<a id="l00137"></a>
<a id="l00138"></a>
<a id="l00140"></a>
<a id="l00141"></a>
<a id="l00143"></a>
<a id="l00144"></a>
<a id="l00146"></a>
<a id="l00147"></a>
<a id="l00148"></a>
<a id="l00149"></a>
<a id="l00150"></a>
<a id="l00154"></a>
<a id="l00155"></a>
<a id="l00156"></a>
<a id="l00157"></a>
<a id="l00158"></a>
<a id="l00159"></a>
<a id="agroup__mcumgr__mgmt__api_html_ga81f98b9a0c3810f7d607b783f8e259b5"></a>
<a id="agroup__mcumgr__mgmt__api_html_gac5d8757a7ca945c77f405764b85ad5c5"></a>
<a id="agroup__mcumgr__mgmt__api_html_gae06a618f492f18e856742b4affab80dd"></a>
<a id="agroup__mcumgr__mgmt__api_html_gga81f98b9a0c3810f7d607b783f8e259b5a0fb725ded4c1e06219549a8bd67b41cb"></a>
<a id="agroup__mcumgr__mgmt__api_html_gga81f98b9a0c3810f7d607b783f8e259b5a1b1c765b0d17e18ceafffe7aabc4644c"></a>
<a id="agroup__mcumgr__mgmt__api_html_gga81f98b9a0c3810f7d607b783f8e259b5a5f7f219d358b67bd30663e176d6be527"></a>
<a id="agroup__mcumgr__mgmt__api_html_gga81f98b9a0c3810f7d607b783f8e259b5a60259d94a32589e521718d100fc5cb2c"></a>
<a id="agroup__mcumgr__mgmt__api_html_gga81f98b9a0c3810f7d607b783f8e259b5a6907de35346ca3af726f6dedaa19b01a"></a>
<a id="agroup__mcumgr__mgmt__api_html_gga81f98b9a0c3810f7d607b783f8e259b5a7cbf80fc5ccf1e5330e4db7e8edaa120"></a>
<a id="agroup__mcumgr__mgmt__api_html_gga81f98b9a0c3810f7d607b783f8e259b5ab8947457860f8a54b4795796b175cd85"></a>
<a id="agroup__mcumgr__mgmt__api_html_gga81f98b9a0c3810f7d607b783f8e259b5abcf72c3092f7aaf88aa11dd5b291a3fc"></a>
<a id="agroup__mcumgr__mgmt__api_html_gga81f98b9a0c3810f7d607b783f8e259b5ac09a1f1ff95f6a913c4c360f1631af68"></a>
<a id="agroup__mcumgr__mgmt__api_html_gga81f98b9a0c3810f7d607b783f8e259b5acf2b9841e28af096820a5dfddc257ca5"></a>
<a id="agroup__mcumgr__mgmt__api_html_gga81f98b9a0c3810f7d607b783f8e259b5ad5273bf46818cd7b6530fb3353ad35f2"></a>
<a id="agroup__mcumgr__mgmt__api_html_gga81f98b9a0c3810f7d607b783f8e259b5af0cff7aeb29cea798688aa3dbf809309"></a>
<a id="agroup__mcumgr__mgmt__api_html_gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726"></a>
<a id="agroup__mcumgr__mgmt__api_html_gga81f98b9a0c3810f7d607b783f8e259b5afaee8ebf655c06b2e7b2a1fe6d45f204"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5a1411ec43d223c8a0765ffc9aabe934b8"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5a16c3e20b3bb42218548fb15d3db144fd"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5a1d37a8c1f0f5618cf192dd8f750ac758"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5a267572964d0db5483ca33e29c5f22fa7"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5a4385d9d027ea3ddd10ae9467ed8ca787"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5a54ad7a80506d328de6b6d0a0e37fad9e"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5a5f234dd0b9781bedcefb5c4627dccb1c"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5a68adbc4d77eaae550973b5169d1c14be"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5a7a0a4726f516645ac8b19efb25f79be1"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5a8145f07e634b5aec368d737dd2a6b054"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5aa43ccd2b916bcf346b202a8e0e5e4bde"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5aa9e253e66d08f08845b2290cd98f68f5"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5ab666f089718b37ada6e2578fa620cb55"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5ac614974c6f88a8b23d9597f54d34b4fe"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggac5d8757a7ca945c77f405764b85ad5c5ae286a84609448fd4465f3ca7cc9bff00"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggae06a618f492f18e856742b4affab80dda4105c10d17622b7de6a8f14c036f3498"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggae06a618f492f18e856742b4affab80dda8dee5baf1e73f1eabccbe8300323e5f9"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggae06a618f492f18e856742b4affab80dda98e8061c8b66effbfee42d79b6e38543"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggae06a618f492f18e856742b4affab80ddac8450257b20fecdaaeab9019434a3fd4"></a>
<a id="agroup__mcumgr__mgmt__api_html_ggae06a618f492f18e856742b4affab80ddad743c94ad3055eb7cf519d88c1d079a7"></a>
<a id="ainttypes_8h_html"></a>

```c
/*
 * Copyright (c) 2018-2021 mcumgr authors
 * Copyright (c) 2022-2023 Nordic Semiconductor ASA
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_MGMT_DEFINES_H_
#define ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_MGMT_DEFINES_H_

#include <inttypes.h>

#ifdef __cplusplus
extern "C" {
#endif


#define MGMT_RETURN_CHECK(ok) ok ? MGMT_ERR_EOK : MGMT_ERR_EMSGSIZE

enum mcumgr_op_t {
        MGMT_OP_READ            = 0,

        MGMT_OP_READ_RSP,

        MGMT_OP_WRITE,

        MGMT_OP_WRITE_RSP,

        MGMT_OP_COUNT,
};

enum mcumgr_group_t {
        MGMT_GROUP_ID_OS        = 0,

        MGMT_GROUP_ID_IMAGE,

        MGMT_GROUP_ID_STAT,

        MGMT_GROUP_ID_SETTINGS,

        MGMT_GROUP_ID_LOG,

        MGMT_GROUP_ID_CRASH,

        MGMT_GROUP_ID_SPLIT,

        MGMT_GROUP_ID_RUN,

        MGMT_GROUP_ID_FS,

        MGMT_GROUP_ID_SHELL,

        MGMT_GROUP_ID_ENUM,

        MGMT_GROUP_ID_TRANSPORT,

        MGMT_GROUP_ID_PERUSER   = 64,

        ZEPHYR_MGMT_GRP_BASIC   = (MGMT_GROUP_ID_PERUSER - 1),
};

enum mcumgr_err_t {
        MGMT_ERR_EOK            = 0,

        MGMT_ERR_EUNKNOWN,

        MGMT_ERR_ENOMEM,

        MGMT_ERR_EINVAL,

        MGMT_ERR_ETIMEOUT,

        MGMT_ERR_ENOENT,

        MGMT_ERR_EBADSTATE,

        MGMT_ERR_EMSGSIZE,

        MGMT_ERR_ENOTSUP,

        MGMT_ERR_ECORRUPT,

        MGMT_ERR_EBUSY,

        MGMT_ERR_EACCESSDENIED,

        MGMT_ERR_UNSUPPORTED_TOO_OLD,

        MGMT_ERR_UNSUPPORTED_TOO_NEW,

        MGMT_ERR_BRIDGED_CONNECTION_UNAVAILABLE,

        MGMT_ERR_EPERUSER       = 256
};

#define MGMT_HDR_SIZE           8


#ifdef __cplusplus
}
#endif

#endif /* ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_MGMT_DEFINES_H_ */
```

## 522.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2018-2021 mcumgr authors。

版权（Copyright）：© 2022-2023 Nordic Semiconductor ASA。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 159 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_MGMT_MCUMGR_MGMT_MGMT_DEFINES_H_`。

## 522.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/mgmt__defines_8h.html)
- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h.html)
- [mcumgr_op_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gae06a618f492f18e856742b4affab80dd)
- [MGMT_OP_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggae06a618f492f18e856742b4affab80ddac8450257b20fecdaaeab9019434a3fd4)
- [MGMT_OP_READ_RSP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggae06a618f492f18e856742b4affab80ddad743c94ad3055eb7cf519d88c1d079a7)
- [MGMT_OP_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggae06a618f492f18e856742b4affab80dda8dee5baf1e73f1eabccbe8300323e5f9)
- [MGMT_OP_WRITE_RSP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggae06a618f492f18e856742b4affab80dda98e8061c8b66effbfee42d79b6e38543)
- [MGMT_OP_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggae06a618f492f18e856742b4affab80dda4105c10d17622b7de6a8f14c036f3498)
- [mcumgr_group_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga81f98b9a0c3810f7d607b783f8e259b5)
- [MGMT_GROUP_ID_OS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5a7cbf80fc5ccf1e5330e4db7e8edaa120)
- [MGMT_GROUP_ID_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5a60259d94a32589e521718d100fc5cb2c)
- [MGMT_GROUP_ID_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5abcf72c3092f7aaf88aa11dd5b291a3fc)
- [MGMT_GROUP_ID_SETTINGS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5a0fb725ded4c1e06219549a8bd67b41cb)
- [MGMT_GROUP_ID_LOG](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5af0cff7aeb29cea798688aa3dbf809309)
- [MGMT_GROUP_ID_CRASH](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5afaee8ebf655c06b2e7b2a1fe6d45f204)
- [MGMT_GROUP_ID_SPLIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5a5f7f219d358b67bd30663e176d6be527)
- [MGMT_GROUP_ID_RUN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5a6907de35346ca3af726f6dedaa19b01a)
- [MGMT_GROUP_ID_FS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5acf2b9841e28af096820a5dfddc257ca5)
- [MGMT_GROUP_ID_SHELL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5ab8947457860f8a54b4795796b175cd85)
- [MGMT_GROUP_ID_ENUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5a1b1c765b0d17e18ceafffe7aabc4644c)
- [MGMT_GROUP_ID_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5ad5273bf46818cd7b6530fb3353ad35f2)
- [MGMT_GROUP_ID_PERUSER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726)
- [ZEPHYR_MGMT_GRP_BASIC](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5ac09a1f1ff95f6a913c4c360f1631af68)
- [mcumgr_err_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gac5d8757a7ca945c77f405764b85ad5c5)
- [MGMT_ERR_EOK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f)
- [MGMT_ERR_EUNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a68adbc4d77eaae550973b5169d1c14be)
- [MGMT_ERR_ENOMEM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5ac614974c6f88a8b23d9597f54d34b4fe)
- [MGMT_ERR_EINVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a267572964d0db5483ca33e29c5f22fa7)
- [MGMT_ERR_ETIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5ab666f089718b37ada6e2578fa620cb55)
- [MGMT_ERR_ENOENT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a54ad7a80506d328de6b6d0a0e37fad9e)
- [MGMT_ERR_EBADSTATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a4385d9d027ea3ddd10ae9467ed8ca787)
- [MGMT_ERR_EMSGSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a16c3e20b3bb42218548fb15d3db144fd)
- [MGMT_ERR_ENOTSUP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a1d37a8c1f0f5618cf192dd8f750ac758)
- [MGMT_ERR_ECORRUPT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5aa9e253e66d08f08845b2290cd98f68f5)
- [MGMT_ERR_EBUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a7a0a4726f516645ac8b19efb25f79be1)
- [MGMT_ERR_EACCESSDENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5aa43ccd2b916bcf346b202a8e0e5e4bde)
- [MGMT_ERR_UNSUPPORTED_TOO_OLD](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a8145f07e634b5aec368d737dd2a6b054)
- [MGMT_ERR_UNSUPPORTED_TOO_NEW](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5ae286a84609448fd4465f3ca7cc9bff00)
- [MGMT_ERR_BRIDGED_CONNECTION_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a5f234dd0b9781bedcefb5c4627dccb1c)
- [MGMT_ERR_EPERUSER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a1411ec43d223c8a0765ffc9aabe934b8)

---

[上一章](P521_mgmt.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P523_mhz19b.h_源码浏览.md)
