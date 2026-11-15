---
id: learning.zephyr-docs.api-file-storage-event-reference.page-3
title: zephyr__mgmt__hawkbit__config.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/config_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_zephyr\_\_mgmt\_\_hawkbit\_\_config.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/config_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

hawkBit配置（Configuration）的头文件。

<a id="details"></a>

```c
#include <stdint.h>
#include <zephyr/net/tls_credentials.h>
```

查看此文件的源码。

hawkBit配置（Configuration）的头文件。

<a id="header-nested-classes"></a>
<a id="nested-classes"></a>

## 3.1\_数据结构（Data Structures）

<a id="r_hawkbit_5Fruntime_5Fconfig"></a>

```c
struct hawkbit_runtime_config
```

相关声明：[hawkbit_runtime_config](../firmware_update/P032_hawkBit运行时配置结构.md)。

HawkBit的配置结构。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.2\_函数（Functions）

<a id="r_ga5e6a1e2e49b75a44a9f13f059ed7d3f6"></a>

```c
int hawkbit_set_config (struct hawkbit_runtime_config *config)
```

相关声明：[hawkbit_set_config](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)、[hawkbit_runtime_config](../firmware_update/P032_hawkBit运行时配置结构.md)。

设置 hawkBit 服务器配置（Server Configuration）。

<a id="r_gaae46014585251b53afe726d42475d739"></a>

```c
struct hawkbit_runtime_config hawkbit_get_config (void)
```

相关声明：[hawkbit_runtime_config](../firmware_update/P032_hawkBit运行时配置结构.md)、[hawkbit_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gaae46014585251b53afe726d42475d739)。

获取 hawkBit 服务器配置（Server Configuration）。

<a id="r_ga2c6aa606a003b34538b521fda77af903"></a>

```c
static int hawkbit_set_server_domain (char *domain_str)
```

相关声明：[hawkbit_set_server_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga2c6aa606a003b34538b521fda77af903)。

设置 hawkBit 服务器主机名（Hostname）。

<a id="r_gaa49efdafe94e1d36a537aff962df41d5"></a>

```c
static int hawkbit_set_server_addr (char *addr_str)
```

相关声明：[hawkbit_set_server_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gaa49efdafe94e1d36a537aff962df41d5)。

设置 hawkBit 服务器地址（Address）。

<a id="r_ga78ef6a168132940040ad04498f0b462d"></a>

```c
static int hawkbit_set_server_port (uint16_t port)
```

相关声明：[hawkbit_set_server_port](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga78ef6a168132940040ad04498f0b462d)、[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)。

设置 hawkBit 服务器端口（Port）。

<a id="r_gaa2799669246cc817bb8e294a8fbfb3d2"></a>

```c
static int hawkbit_set_ddi_security_token (char *token)
```

相关声明：[hawkbit_set_ddi_security_token](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gaa2799669246cc817bb8e294a8fbfb3d2)。

设置 hawkBit 安全令牌（Security Token）。

<a id="r_ga5c73e9ba4dd9788e22fdb11f1f2b81ee"></a>

```c
static int hawkbit_set_tls_tag (sec_tag_t tag)
```

相关声明：[hawkbit_set_tls_tag](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga5c73e9ba4dd9788e22fdb11f1f2b81ee)、[sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)。

设置 hawkBit TLS 标签（Tag）。

<a id="r_gacbbaed38e2ace7d8dcc78e40b286b5e9"></a>

```c
static char * hawkbit_get_server_addr (void)
```

相关声明：[hawkbit_get_server_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gacbbaed38e2ace7d8dcc78e40b286b5e9)。

获取 hawkBit 服务器地址（Address）。

<a id="r_gafd9f30b2acab65c34bcb5edaa3da8738"></a>

```c
static char * hawkbit_get_server_domain (void)
```

相关声明：[hawkbit_get_server_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gafd9f30b2acab65c34bcb5edaa3da8738)。

获取 hawkBit 服务器主机名（Hostname）。

<a id="r_ga3674fc406aa20fe4770ff0c729817b7c"></a>

```c
static uint16_t hawkbit_get_server_port (void)
```

相关声明：[uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)、[hawkbit_get_server_port](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga3674fc406aa20fe4770ff0c729817b7c)。

获取 hawkBit 服务器端口（Port）。

<a id="r_gadc4aea2dac4915a434a10e6e055f54f7"></a>

```c
static char * hawkbit_get_ddi_security_token (void)
```

相关声明：[hawkbit_get_ddi_security_token](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gadc4aea2dac4915a434a10e6e055f54f7)。

获取 hawkBit 安全令牌（Security Token）。

<a id="r_ga694e5f4fbcae451eb90a019f6d1f3b81"></a>

```c
static sec_tag_t hawkbit_get_tls_tag (void)
```

相关声明：[sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)、[hawkbit_get_tls_tag](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga694e5f4fbcae451eb90a019f6d1f3b81)。

获取 hawkBit TLS 标签（Tag）。

<a id="r_ga0ca5f633e902137ecda068ab312d52db"></a>

```c
int32_t hawkbit_get_action_id (void)
```

相关声明：[int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)、[hawkbit_get_action_id](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga0ca5f633e902137ecda068ab312d52db)。

获取 hawkBit 操作 ID（Action ID）。

<a id="r_ga46c56cee1a89abd81a328ef3f91648bb"></a>

```c
uint32_t hawkbit_get_poll_interval (void)
```

相关声明：[uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)、[hawkbit_get_poll_interval](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga46c56cee1a89abd81a328ef3f91648bb)。

获取 hawkBit 轮询间隔（Poll Interval）。


## 3.3\_原页交叉引用（Cross References）

- [stdint.h](../api_source_device_reference/P036_stdint.h_源码浏览.md)
- [zephyr/net/tls_credentials.h](../api_source_reference/P870_tls_credentials.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P111_config.h_源码浏览.md)
- [hawkbit_runtime_config](../firmware_update/P032_hawkBit运行时配置结构.md)
- [hawkbit_set_config](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga5e6a1e2e49b75a44a9f13f059ed7d3f6)
- [hawkbit_get_config](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gaae46014585251b53afe726d42475d739)
- [hawkbit_set_server_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga2c6aa606a003b34538b521fda77af903)
- [hawkbit_set_server_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gaa49efdafe94e1d36a537aff962df41d5)
- [hawkbit_set_server_port](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga78ef6a168132940040ad04498f0b462d)
- [uint16_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a5debae8b2a1ec20a6694c0c443ee399e)
- [hawkbit_set_ddi_security_token](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gaa2799669246cc817bb8e294a8fbfb3d2)
- [hawkbit_set_tls_tag](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga5c73e9ba4dd9788e22fdb11f1f2b81ee)
- [sec_tag_t](https://docs.zephyrproject.org/latest/doxygen/html/group__tls__credentials.html#gaadfe9694309e473f7be74ed98dfb36d3)
- [hawkbit_get_server_addr](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gacbbaed38e2ace7d8dcc78e40b286b5e9)
- [hawkbit_get_server_domain](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gafd9f30b2acab65c34bcb5edaa3da8738)
- [hawkbit_get_server_port](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga3674fc406aa20fe4770ff0c729817b7c)
- [hawkbit_get_ddi_security_token](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#gadc4aea2dac4915a434a10e6e055f54f7)
- [hawkbit_get_tls_tag](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga694e5f4fbcae451eb90a019f6d1f3b81)
- [int32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0c18914b3041c2f583aba76f418399c2)
- [hawkbit_get_action_id](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga0ca5f633e902137ecda068ab312d52db)
- [uint32_t](../api_file_reference/P408_____w__zephyr__zephyr__lib__libc__minimal__include__stdint.h_文件参考.md#a0a8582351ac627ee8bde2973c825e47f)
- [hawkbit_get_poll_interval](https://docs.zephyrproject.org/latest/doxygen/html/group__hawkbit__config.html#ga46c56cee1a89abd81a328ef3f91648bb)

<a id="header-details"></a>

---

[上一章](P002_zephyr__drivers__can__can_fake.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P004_zephyr__bluetooth__services__cts.h_文件参考.md)
