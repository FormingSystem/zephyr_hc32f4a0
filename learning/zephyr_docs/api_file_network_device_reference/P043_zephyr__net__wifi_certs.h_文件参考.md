---
id: learning.zephyr-docs.api-file-network-device-reference.page-43
title: zephyr__net__wifi_certs.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/wifi__certs_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第43章\_zephyr\_\_net\_\_wifi\_certs.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/wifi__certs_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

Wi-Fi企业模式凭据设置（Enterprise Mode Credentials Setup）的API。

<a id="details"></a>

```c
#include <stdbool.h>
#include <zephyr/kernel.h>
#include <zephyr/net/wifi_mgmt.h>
```

查看此文件的源码。

Wi-Fi企业模式凭据设置（Enterprise Mode Credentials Setup）的API。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 43.1\_函数（Functions）

<a id="r_a21f62e407bc403636fbe6ed973e620f6"></a>

```c
int wifi_set_enterprise_credentials (struct net_if *iface, bool is_ap)
```

相关声明：[wifi_set_enterprise_credentials](#a21f62e407bc403636fbe6ed973e620f6)、[net_if](../network_core_model_reference/P079_net_if_结构体.md)、[bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)。

设置 Wi-Fi 企业模式凭据（Enterprise Credentials）。

<a id="r_a1ed064792c11d2760b6b5c3dfdaabe82"></a>

```c
void wifi_clear_enterprise_credentials (void)
```

相关声明：[wifi_clear_enterprise_credentials](#a1ed064792c11d2760b6b5c3dfdaabe82)。

清除 Wi-Fi 企业模式凭据（Enterprise Credentials）。

## 43.2\_详细说明（Detailed Documentation）

<a id="a1ed064792c11d2760b6b5c3dfdaabe82"></a>

### `wifi_clear_enterprise_credentials()`

```c
void wifi_clear_enterprise_credentials ( void )
```

清除 Wi-Fi 企业模式凭据（Enterprise Credentials）。

<a id="a21f62e407bc403636fbe6ed973e620f6"></a>

### `wifi_set_enterprise_credentials()`

```c
int wifi_set_enterprise_credentials ( struct net_if * iface, bool is_ap )
```

设置 Wi-Fi 企业模式凭据（Enterprise Credentials）。

为接入点（Access Point）和站点（Station）模式配置企业模式（Enterprise Mode）所需的凭据。

通常使用的证书（Certificates）：

- 证书颁发机构证书（CA Certificate）。
- 客户端证书（Client Certificate）。
- 客户端私钥（Client Private Key）。
- 服务器证书和服务器密钥（Server Certificate and Server Key），用于接入点（AP）模式。

**参数（Parameters）**

| 名称／方向 | 说明 |
| --- | --- |
| `iface` | 网络接口（Network Interface） |
| `is_ap` | 接入点（AP）或站点（Station）模式。 |

**返回（Returns）**：返回值（Returns）：成功时为 `0`，发生错误时小于 `0`。


## 43.3\_原页交叉引用（Cross References）

- [stdbool.h](../api_source_supplement_reference/P186_stdbool.h_源码浏览.md)
- [zephyr/kernel.h](../api_source_workqueue_pin_control_reference/P002_kernel.h_源码浏览.md)
- [zephyr/net/wifi_mgmt.h](../api_source_http_wifi_reference/P009_wifi_mgmt.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P917_wifi_certs.h_源码浏览.md)
- [net_if](../network_core_model_reference/P079_net_if_结构体.md)
- [bool](../api_file_reference/P407_____w__zephyr__zephyr__lib__libc__minimal__include__stdbool.h_文件参考.md#abb452686968e48b67397da5f97445f5b)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P042_zephyr__drivers__sensor__vl53l0x.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P044_zephyr__net__wifi_nm.h_文件参考.md)
