---
id: learning.zephyr-docs.api-source-reference.page-430
title: keygen.h_源码浏览
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/keygen_8h_source.html
---

<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第430章\_keygen.h\_源码浏览

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/keygen_8h_source.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

本页保留官方 Doxygen 源码浏览页的全部可见代码与注释，仅去除展示行号、还原展示用不换行空格并清除行尾空白。Doxygen 会省略已用于生成接口说明的部分文档注释，因此原行号可能跳跃。下方译文覆盖本页全部可见注释；函数、参数、返回值及宏定义说明见[对应文件参考](https://docs.zephyrproject.org/latest/doxygen/html/keygen_8h.html)。

## 430.1\_原始可见代码（Source Code）

<a id="l00001"></a>
<a id="l00002"></a>
<a id="l00003"></a>
<a id="l00004"></a>
<a id="l00005"></a>
<a id="l00006"></a>
<a id="l00007"></a>
<a id="l00008"></a>
<a id="l00009"></a>
<a id="l00021"></a>
<a id="l00022"></a>
<a id="l00023"></a>
<a id="l00024"></a>
<a id="l00025"></a>
<a id="l00026"></a>
<a id="l00027"></a>
<a id="foldopen00029"></a>
<a id="l00029"></a>
<a id="l00031"></a>
<a id="l00032"></a>
<a id="l00033"></a>
<a id="foldopen00035"></a>
<a id="l00035"></a>
<a id="l00037"></a>
<a id="l00039"></a>
<a id="l00040"></a>
<a id="l00041"></a>
<a id="l00053"></a>
<a id="l00054"></a>
<a id="l00055"></a>
<a id="l00056"></a>
<a id="l00071"></a>
<a id="l00072"></a>
<a id="l00073"></a>
<a id="l00074"></a>
<a id="l00075"></a>
<a id="l00076"></a>
<a id="l00090"></a>
<a id="l00091"></a>
<a id="l00092"></a>
<a id="l00093"></a>
<a id="l00094"></a>
<a id="l00095"></a>
<a id="l00104"></a>
<a id="l00105"></a>
<a id="l00106"></a>
<a id="l00107"></a>
<a id="l00108"></a>
<a id="l00109"></a>
<a id="l00113"></a>
<a id="l00114"></a>
<a id="agroup__ssh__keygen_html_ga04750b02826f13fe5b2e5f18b00502eb"></a>
<a id="agroup__ssh__keygen_html_ga233f6b99069e88b2fd16dd0fda0a25d2"></a>
<a id="agroup__ssh__keygen_html_ga2a7b4b68a5ac02a60f92d4f05f6adcd6"></a>
<a id="agroup__ssh__keygen_html_ga527dec6fda5f6d56214f12d708c1b5d4"></a>
<a id="agroup__ssh__keygen_html_ga7447ca57ca8a3ff9a2f7dd024cfe338e"></a>
<a id="agroup__ssh__keygen_html_gac37edb233d0cf4c3ea3a07d89e26dbdc"></a>
<a id="agroup__ssh__keygen_html_gga233f6b99069e88b2fd16dd0fda0a25d2a1215ac3bb911207c3e31e7935a341a0a"></a>
<a id="agroup__ssh__keygen_html_gga527dec6fda5f6d56214f12d708c1b5d4ac14e3b8241a8da8d555144c38e889cfc"></a>
<a id="agroup__ssh__keygen_html_gga527dec6fda5f6d56214f12d708c1b5d4ac84b189d99a0ad42c97a0125e4662d92"></a>
<a id="akernel_8h_html"></a>

```c
/*
 * Copyright (c) 2024 Grant Ramsay <grant.ramsay@hotmail.com>
 *
 * SPDX-License-Identifier: Apache-2.0
 */

#ifndef ZEPHYR_INCLUDE_NET_SSH_KEYGEN_H_
#define ZEPHYR_INCLUDE_NET_SSH_KEYGEN_H_


#include <zephyr/kernel.h>

#ifdef __cplusplus
extern "C" {
#endif

enum ssh_host_key_type {
        SSH_HOST_KEY_TYPE_RSA,
};

enum ssh_host_key_format {
        SSH_HOST_KEY_FORMAT_DER,
        SSH_HOST_KEY_FORMAT_PEM,
};

int ssh_keygen(int key_index,
               enum ssh_host_key_type key_type,
               size_t key_size_bits);

int ssh_keygen_export(int key_index,
                      bool private_key,
                      enum ssh_host_key_format fmt,
                      void *buf,
                      size_t buf_len);

int ssh_keygen_import(int key_index,
                      bool private_key,
                      enum ssh_host_key_format fmt,
                      const void *buf,
                      size_t buf_len);

int ssh_keygen_free(int key_index);

#ifdef __cplusplus
}
#endif


#endif /* ZEPHYR_INCLUDE_NET_SSH_KEYGEN_H_ */
```

## 430.2\_可见注释译文（Comments）

### 注释 1：原第 1 行

版权（Copyright）：© 2024 Grant Ramsay <grant.ramsay@hotmail.com>。

SPDX 许可证标识（License Identifier）：`Apache-2.0`。

### 注释 2：原第 114 行

头文件保护宏（Header guard）标记：`ZEPHYR_INCLUDE_NET_SSH_KEYGEN_H_`。

## 430.3\_原页交叉引用（Cross References）

- [查看此文件的参考说明](https://docs.zephyrproject.org/latest/doxygen/html/keygen_8h.html)
- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)
- [ssh_host_key_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga233f6b99069e88b2fd16dd0fda0a25d2)
- [SSH_HOST_KEY_TYPE_RSA](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#gga233f6b99069e88b2fd16dd0fda0a25d2a1215ac3bb911207c3e31e7935a341a0a)
- [ssh_host_key_format](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga527dec6fda5f6d56214f12d708c1b5d4)
- [SSH_HOST_KEY_FORMAT_DER](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#gga527dec6fda5f6d56214f12d708c1b5d4ac14e3b8241a8da8d555144c38e889cfc)
- [SSH_HOST_KEY_FORMAT_PEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#gga527dec6fda5f6d56214f12d708c1b5d4ac84b189d99a0ad42c97a0125e4662d92)
- [ssh_keygen](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga2a7b4b68a5ac02a60f92d4f05f6adcd6)
- [ssh_keygen_export](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga04750b02826f13fe5b2e5f18b00502eb)
- [ssh_keygen_import](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga7447ca57ca8a3ff9a2f7dd024cfe338e)
- [ssh_keygen_free](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#gac37edb233d0cf4c3ea3a07d89e26dbdc)
- [kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h.html)

---

[上一章](P429_key_ids.h_源码浏览.md) · [返回大纲](大纲.md) · [下一章](P431_keymap.h_源码浏览.md)
