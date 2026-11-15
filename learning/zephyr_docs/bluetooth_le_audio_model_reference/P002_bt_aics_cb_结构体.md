---
id: learning.zephyr-docs.bluetooth-le-audio-model-reference.page-2
title: bt_aics_cb_结构体
kind: reference
status: maintained
domains: [zephyr, bluetooth, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/structbt__aics__cb.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第2章\_bt\_aics\_cb\_结构体

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/structbt__aics__cb.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

保存音频输入控制服务（AICS）回调的结构体。

```c
#include <zephyr/bluetooth/audio/aics.h>
```

<a id="details"></a>

保存音频输入控制服务（AICS）回调的结构体，客户端和服务器均使用它。

<a id="header-pub-attribs"></a>
<a id="pub-attribs"></a>

## 2.1\_数据成员（Data Fields）

<a id="r_a70d099bec6407e5c92f6a4e8d6c44929"></a>

```c
bt_aics_state_cb state
```

相关声明：[bt_aics_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga2e851f49f9c7e71a18376468a13fdf4f)、[state](#a70d099bec6407e5c92f6a4e8d6c44929)。

音频输入状态（Audio Input State）已变化。

<a id="r_a6b2f2a43d0a91abcecfe8372b6a1be4b"></a>

```c
bt_aics_gain_setting_cb gain_setting
```

相关声明：[bt_aics_gain_setting_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga11da08c010f4aa849c2e3725dc5cbaeb)、[gain_setting](#a6b2f2a43d0a91abcecfe8372b6a1be4b)。

增益设置（Gain Setting）已变化。

<a id="r_a41bc7a97e28c53772573d99a38e8ac55"></a>

```c
bt_aics_type_cb type
```

相关声明：[bt_aics_type_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga6e76b9f2de4cdbcd7539c76f6a347fa5)、[type](#a41bc7a97e28c53772573d99a38e8ac55)。

音频输入类型已变化。

<a id="r_ac89882943c293e533bec55dd285d7aa0"></a>

```c
bt_aics_status_cb status
```

相关声明：[bt_aics_status_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga044d92a4273c6537a9cdf20922352ed6)、[status](#ac89882943c293e533bec55dd285d7aa0)。

音频输入活动状态（Audio Input Status）已变化。

<a id="r_ad37ae465600fa2e3c1868f0da07fd31a"></a>

```c
bt_aics_description_cb description
```

相关声明：[bt_aics_description_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga98b142ea7a66de5577c44aa90d507930)、[description](#ad37ae465600fa2e3c1868f0da07fd31a)。

音频输入描述已变化。

<a id="r_ae946f4b434b485774a3c8ddca5d86898"></a>

```c
bt_aics_discover_cb discover
```

相关声明：[bt_aics_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga9fda39f8410308e05eb928eeb7267e83)、[discover](#ae946f4b434b485774a3c8ddca5d86898)。

发现（Discovery）已完成。

<a id="r_a1f13bdcfbfac65800f9e66dad48c3b78"></a>

```c
bt_aics_write_cb set_gain
```

相关声明：[bt_aics_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga36991fe1dee5168db618518d094d80ef)、[set_gain](#a1f13bdcfbfac65800f9e66dad48c3b78)。

设置增益操作已完成。

<a id="r_a80c8abd842706d2588e6a075cba61ba8"></a>

```c
bt_aics_write_cb unmute
```

相关声明：[bt_aics_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga36991fe1dee5168db618518d094d80ef)、[unmute](#a80c8abd842706d2588e6a075cba61ba8)。

取消静音（Unmute）操作已完成。

<a id="r_a41b6cac6ccc0195921d2e5a127d9091d"></a>

```c
bt_aics_write_cb mute
```

相关声明：[bt_aics_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga36991fe1dee5168db618518d094d80ef)、[mute](#a41b6cac6ccc0195921d2e5a127d9091d)。

静音（Mute）操作已完成。

<a id="r_a1b54464a8c6df54993914da97da2f93d"></a>

```c
bt_aics_write_cb set_manual_mode
```

相关声明：[bt_aics_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga36991fe1dee5168db618518d094d80ef)、[set_manual_mode](#a1b54464a8c6df54993914da97da2f93d)。

设置手动模式（Manual Mode）操作已完成。

<a id="r_aac9dccf825f5aa423212af4af3d4ca38"></a>

```c
bt_aics_write_cb set_auto_mode
```

相关声明：[bt_aics_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga36991fe1dee5168db618518d094d80ef)、[set_auto_mode](#aac9dccf825f5aa423212af4af3d4ca38)。

设置自动模式（Automatic Mode）已完成。

## 2.2\_详细说明（Detailed Documentation）

<a id="ad37ae465600fa2e3c1868f0da07fd31a"></a>

### `description`

```c
bt_aics_description_cb bt_aics_cb::description
```

音频输入描述已变化。

<a id="ae946f4b434b485774a3c8ddca5d86898"></a>

### `discover`

```c
bt_aics_discover_cb bt_aics_cb::discover
```

发现（Discovery）已完成。

<a id="a6b2f2a43d0a91abcecfe8372b6a1be4b"></a>

### `gain_setting`

```c
bt_aics_gain_setting_cb bt_aics_cb::gain_setting
```

增益设置（Gain Setting）已变化。

<a id="a41b6cac6ccc0195921d2e5a127d9091d"></a>

### `mute`

```c
bt_aics_write_cb bt_aics_cb::mute
```

静音（Mute）操作已完成。

<a id="aac9dccf825f5aa423212af4af3d4ca38"></a>

### `set_auto_mode`

```c
bt_aics_write_cb bt_aics_cb::set_auto_mode
```

设置自动模式（Automatic Mode）已完成。

<a id="a1f13bdcfbfac65800f9e66dad48c3b78"></a>

### `set_gain`

```c
bt_aics_write_cb bt_aics_cb::set_gain
```

设置增益操作已完成。

<a id="a1b54464a8c6df54993914da97da2f93d"></a>

### `set_manual_mode`

```c
bt_aics_write_cb bt_aics_cb::set_manual_mode
```

设置手动模式（Manual Mode）操作已完成。

<a id="a70d099bec6407e5c92f6a4e8d6c44929"></a>

### `state`

```c
bt_aics_state_cb bt_aics_cb::state
```

音频输入状态（Audio Input State）已变化。

<a id="ac89882943c293e533bec55dd285d7aa0"></a>

### `status`

```c
bt_aics_status_cb bt_aics_cb::status
```

音频输入活动状态（Audio Input Status）已变化。

<a id="a41bc7a97e28c53772573d99a38e8ac55"></a>

### `type`

```c
bt_aics_type_cb bt_aics_cb::type
```

音频输入类型已变化。

<a id="a80c8abd842706d2588e6a075cba61ba8"></a>

### `unmute`

```c
bt_aics_write_cb bt_aics_cb::unmute
```

取消静音（Unmute）操作已完成。

本结构体文档由以下文件生成：

- `zephyr/bluetooth/audio/aics.h`

## 2.3\_原页交叉引用（Cross References）

- [zephyr/bluetooth/audio/aics.h](https://docs.zephyrproject.org/latest/doxygen/html/aics_8h_source.html)
- [bt_aics_state_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga2e851f49f9c7e71a18376468a13fdf4f)
- [bt_aics_gain_setting_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga11da08c010f4aa849c2e3725dc5cbaeb)
- [bt_aics_type_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga6e76b9f2de4cdbcd7539c76f6a347fa5)
- [bt_aics_status_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga044d92a4273c6537a9cdf20922352ed6)
- [bt_aics_description_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga98b142ea7a66de5577c44aa90d507930)
- [bt_aics_discover_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga9fda39f8410308e05eb928eeb7267e83)
- [bt_aics_write_cb](https://docs.zephyrproject.org/latest/doxygen/html/group__bt__aics.html#ga36991fe1dee5168db618518d094d80ef)

<a id="header-details"></a>
<a id="doc-variable-members"></a>
<a id="header-doc-variable-members"></a>

---

[上一章](P001_bt_aics_结构体.md) · [返回大纲](大纲.md) · [下一章](P003_bt_aics_discover_param_结构体.md)
