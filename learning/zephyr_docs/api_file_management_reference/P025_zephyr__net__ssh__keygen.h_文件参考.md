---
id: learning.zephyr-docs.api-file-management-reference.page-25
title: zephyr__net__ssh__keygen.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/keygen_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第25章\_zephyr\_\_net\_\_ssh\_\_keygen.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/keygen_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

安全Shell（SSH）密钥生成（Keygen）的API。

<a id="details"></a>

```c
#include <zephyr/kernel.h>
```

查看此文件的源码。

安全Shell（SSH）密钥生成（Keygen）的API。

<a id="header-enum-members"></a>
<a id="enum-members"></a>

## 25.1\_枚举（Enumerations）

<a id="r_ga233f6b99069e88b2fd16dd0fda0a25d2"></a>

```c
enum ssh_host_key_type { SSH_HOST_KEY_TYPE_RSA }
```

相关声明：[ssh_host_key_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga233f6b99069e88b2fd16dd0fda0a25d2)、[SSH_HOST_KEY_TYPE_RSA](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#gga233f6b99069e88b2fd16dd0fda0a25d2a1215ac3bb911207c3e31e7935a341a0a)。

可生成的主机密钥（host keys）类型。

<a id="r_ga527dec6fda5f6d56214f12d708c1b5d4"></a>

```c
enum ssh_host_key_format { SSH_HOST_KEY_FORMAT_DER , SSH_HOST_KEY_FORMAT_PEM }
```

相关声明：[ssh_host_key_format](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga527dec6fda5f6d56214f12d708c1b5d4)、[SSH_HOST_KEY_FORMAT_DER](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#gga527dec6fda5f6d56214f12d708c1b5d4ac14e3b8241a8da8d555144c38e889cfc)、[SSH_HOST_KEY_FORMAT_PEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#gga527dec6fda5f6d56214f12d708c1b5d4ac84b189d99a0ad42c97a0125e4662d92)。

SSH 主机密钥可导出／导入的格式。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 25.2\_函数（Functions）

<a id="r_ga2a7b4b68a5ac02a60f92d4f05f6adcd6"></a>

```c
int ssh_keygen (int key_index, enum ssh_host_key_type key_type, size_t key_size_bits)
```

相关声明：[ssh_keygen](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga2a7b4b68a5ac02a60f92d4f05f6adcd6)、[ssh_host_key_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga233f6b99069e88b2fd16dd0fda0a25d2)。

生成新的 SSH 主机密钥。

<a id="r_ga04750b02826f13fe5b2e5f18b00502eb"></a>

```c
int ssh_keygen_export (int key_index, bool private_key, enum ssh_host_key_format fmt, void *buf, size_t buf_len)
```

相关声明：[ssh_keygen_export](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga04750b02826f13fe5b2e5f18b00502eb)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[ssh_host_key_format](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga527dec6fda5f6d56214f12d708c1b5d4)。

导出已生成的 SSH 主机密钥。

<a id="r_ga7447ca57ca8a3ff9a2f7dd024cfe338e"></a>

```c
int ssh_keygen_import (int key_index, bool private_key, enum ssh_host_key_format fmt, const void *buf, size_t buf_len)
```

相关声明：[ssh_keygen_import](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga7447ca57ca8a3ff9a2f7dd024cfe338e)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)、[ssh_host_key_format](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga527dec6fda5f6d56214f12d708c1b5d4)。

导入 SSH 主机密钥。

<a id="r_gac37edb233d0cf4c3ea3a07d89e26dbdc"></a>

```c
int ssh_keygen_free (int key_index)
```

相关声明：[ssh_keygen_free](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#gac37edb233d0cf4c3ea3a07d89e26dbdc)。

释放已生成的 SSH 主机密钥。


## 25.3\_原页交叉引用（Cross References）

- [zephyr/kernel.h](https://docs.zephyrproject.org/latest/doxygen/html/kernel_8h_source.html)
- [查看此文件的源码。](../api_source_reference/P430_keygen.h_源码浏览.md)
- [ssh_host_key_type](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga233f6b99069e88b2fd16dd0fda0a25d2)
- [SSH_HOST_KEY_TYPE_RSA](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#gga233f6b99069e88b2fd16dd0fda0a25d2a1215ac3bb911207c3e31e7935a341a0a)
- [ssh_host_key_format](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga527dec6fda5f6d56214f12d708c1b5d4)
- [SSH_HOST_KEY_FORMAT_DER](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#gga527dec6fda5f6d56214f12d708c1b5d4ac14e3b8241a8da8d555144c38e889cfc)
- [SSH_HOST_KEY_FORMAT_PEM](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#gga527dec6fda5f6d56214f12d708c1b5d4ac84b189d99a0ad42c97a0125e4662d92)
- [ssh_keygen](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga2a7b4b68a5ac02a60f92d4f05f6adcd6)
- [ssh_keygen_export](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga04750b02826f13fe5b2e5f18b00502eb)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)
- [ssh_keygen_import](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#ga7447ca57ca8a3ff9a2f7dd024cfe338e)
- [ssh_keygen_free](https://docs.zephyrproject.org/latest/doxygen/html/group__ssh__keygen.html#gac37edb233d0cf4c3ea3a07d89e26dbdc)

<a id="header-details"></a>

---

[上一章](P024_zephyr__drivers__flash__it51xxx_flash_api_ex.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P026_zephyr__bluetooth__audio__lc3.h_文件参考.md)
