---
id: learning.zephyr-docs.api-file-service-reference.page-22
title: zephyr__mgmt__mcumgr__mgmt__mgmt_defines.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/mgmt__defines_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第22章\_zephyr\_\_mgmt\_\_mcumgr\_\_mgmt\_\_mgmt\_defines.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/mgmt__defines_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

```c
#include <inttypes.h>
```

查看此文件的源码。

<a id="header-define-members"></a>
<a id="define-members"></a>

## 22.1\_宏定义（Macros）

<a id="r_gabdd715ff5b7efe040f205edf0b00bc43"></a>

```c
#define MGMT_RETURN_CHECK(ok)
```

相关声明：[MGMT_RETURN_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gabdd715ff5b7efe040f205edf0b00bc43)。

在 MCUmgr 处理器（Handlers）的末尾使用：若达到消息大小限制（Message Size Limit），则返回错误；否则返回成功（OK）。

<a id="r_gabb62e7697ffb2a2f4e6d96abe28808a6"></a>

```c
#define MGMT_HDR_SIZE 8
```

相关声明：[MGMT_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gabb62e7697ffb2a2f4e6d96abe28808a6)。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 22.2\_枚举（Enumerations）

<a id="r_gae06a618f492f18e856742b4affab80dd"></a>

```c
enum mcumgr_op_t { MGMT_OP_READ = 0 , MGMT_OP_READ_RSP , MGMT_OP_WRITE , MGMT_OP_WRITE_RSP , MGMT_OP_COUNT }
```

相关声明：[mcumgr_op_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gae06a618f492f18e856742b4affab80dd)、[MGMT_OP_READ](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggae06a618f492f18e856742b4affab80ddac8450257b20fecdaaeab9019434a3fd4)、[MGMT_OP_READ_RSP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggae06a618f492f18e856742b4affab80ddad743c94ad3055eb7cf519d88c1d079a7)、[MGMT_OP_WRITE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggae06a618f492f18e856742b4affab80dda8dee5baf1e73f1eabccbe8300323e5f9)、[MGMT_OP_WRITE_RSP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggae06a618f492f18e856742b4affab80dda98e8061c8b66effbfee42d79b6e38543)、[MGMT_OP_COUNT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggae06a618f492f18e856742b4affab80dda4105c10d17622b7de6a8f14c036f3498)。

操作码（Opcodes），编码于头部（Header）的第一个字节中。

<a id="r_ga81f98b9a0c3810f7d607b783f8e259b5"></a>

```c
enum mcumgr_group_t { MGMT_GROUP_ID_OS = 0 , MGMT_GROUP_ID_IMAGE , MGMT_GROUP_ID_STAT , MGMT_GROUP_ID_SETTINGS , MGMT_GROUP_ID_LOG , MGMT_GROUP_ID_CRASH , MGMT_GROUP_ID_SPLIT , MGMT_GROUP_ID_RUN , MGMT_GROUP_ID_FS , MGMT_GROUP_ID_SHELL , MGMT_GROUP_ID_ENUM , MGMT_GROUP_ID_TRANSPORT , MGMT_GROUP_ID_PERUSER = 64 , ZEPHYR_MGMT_GRP_BASIC = (MGMT_GROUP_ID_PERUSER - 1) }
```

相关声明：[mcumgr_group_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ga81f98b9a0c3810f7d607b783f8e259b5)、[MGMT_GROUP_ID_OS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5a7cbf80fc5ccf1e5330e4db7e8edaa120)、[MGMT_GROUP_ID_IMAGE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5a60259d94a32589e521718d100fc5cb2c)、[MGMT_GROUP_ID_STAT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5abcf72c3092f7aaf88aa11dd5b291a3fc)、[MGMT_GROUP_ID_SETTINGS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5a0fb725ded4c1e06219549a8bd67b41cb)、[MGMT_GROUP_ID_LOG](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5af0cff7aeb29cea798688aa3dbf809309)、[MGMT_GROUP_ID_CRASH](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5afaee8ebf655c06b2e7b2a1fe6d45f204)、[MGMT_GROUP_ID_SPLIT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5a5f7f219d358b67bd30663e176d6be527)、[MGMT_GROUP_ID_RUN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5a6907de35346ca3af726f6dedaa19b01a)、[MGMT_GROUP_ID_FS](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5acf2b9841e28af096820a5dfddc257ca5)、[MGMT_GROUP_ID_SHELL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5ab8947457860f8a54b4795796b175cd85)、[MGMT_GROUP_ID_ENUM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5a1b1c765b0d17e18ceafffe7aabc4644c)、[MGMT_GROUP_ID_TRANSPORT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5ad5273bf46818cd7b6530fb3353ad35f2)、[MGMT_GROUP_ID_PERUSER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5af2504389290c7b2a3537f4ebfb730726)、[ZEPHYR_MGMT_GRP_BASIC](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gga81f98b9a0c3810f7d607b783f8e259b5ac09a1f1ff95f6a913c4c360f1631af68)。

MCUmgr 组（Groups）。

<a id="r_gac5d8757a7ca945c77f405764b85ad5c5"></a>

```c
enum mcumgr_err_t { MGMT_ERR_EOK = 0 , MGMT_ERR_EUNKNOWN , MGMT_ERR_ENOMEM , MGMT_ERR_EINVAL , MGMT_ERR_ETIMEOUT , MGMT_ERR_ENOENT , MGMT_ERR_EBADSTATE , MGMT_ERR_EMSGSIZE , MGMT_ERR_ENOTSUP , MGMT_ERR_ECORRUPT , MGMT_ERR_EBUSY , MGMT_ERR_EACCESSDENIED , MGMT_ERR_UNSUPPORTED_TOO_OLD , MGMT_ERR_UNSUPPORTED_TOO_NEW , MGMT_ERR_BRIDGED_CONNECTION_UNAVAILABLE , MGMT_ERR_EPERUSER = 256 }
```

相关声明：[mcumgr_err_t](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gac5d8757a7ca945c77f405764b85ad5c5)、[MGMT_ERR_EOK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a4201fc6fbffd1ca9ae99a2e90a40896f)、[MGMT_ERR_EUNKNOWN](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a68adbc4d77eaae550973b5169d1c14be)、[MGMT_ERR_ENOMEM](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5ac614974c6f88a8b23d9597f54d34b4fe)、[MGMT_ERR_EINVAL](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a267572964d0db5483ca33e29c5f22fa7)、[MGMT_ERR_ETIMEOUT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5ab666f089718b37ada6e2578fa620cb55)、[MGMT_ERR_ENOENT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a54ad7a80506d328de6b6d0a0e37fad9e)、[MGMT_ERR_EBADSTATE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a4385d9d027ea3ddd10ae9467ed8ca787)、[MGMT_ERR_EMSGSIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a16c3e20b3bb42218548fb15d3db144fd)、[MGMT_ERR_ENOTSUP](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a1d37a8c1f0f5618cf192dd8f750ac758)、[MGMT_ERR_ECORRUPT](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5aa9e253e66d08f08845b2290cd98f68f5)、[MGMT_ERR_EBUSY](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a7a0a4726f516645ac8b19efb25f79be1)、[MGMT_ERR_EACCESSDENIED](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5aa43ccd2b916bcf346b202a8e0e5e4bde)、[MGMT_ERR_UNSUPPORTED_TOO_OLD](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a8145f07e634b5aec368d737dd2a6b054)、[MGMT_ERR_UNSUPPORTED_TOO_NEW](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5ae286a84609448fd4465f3ca7cc9bff00)、[MGMT_ERR_BRIDGED_CONNECTION_UNAVAILABLE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a5f234dd0b9781bedcefb5c4627dccb1c)、[MGMT_ERR_EPERUSER](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#ggac5d8757a7ca945c77f405764b85ad5c5a1411ec43d223c8a0765ffc9aabe934b8)。

MCUmgr 错误码（Error Codes）。


## 22.3\_原页交叉引用（Cross References）

- [inttypes.h](https://docs.zephyrproject.org/latest/doxygen/html/inttypes_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P522_mgmt_defines.h_源码浏览.md)
- [MGMT_RETURN_CHECK](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gabdd715ff5b7efe040f205edf0b00bc43)
- [MGMT_HDR_SIZE](https://docs.zephyrproject.org/latest/doxygen/html/group__mcumgr__mgmt__api.html#gabb62e7697ffb2a2f4e6d96abe28808a6)
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

[上一章](P021_zephyr__drivers__mfd__mfd_maxq10xx.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P023_zephyr__mpipe__mpipe_bin.h_文件参考.md)
