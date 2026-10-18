---
id: learning.zephyr-docs.api-file-system-device-reference.page-52
title: zephyr__bluetooth__testing.h_文件参考
kind: reference
status: maintained
domains: [zephyr, drivers, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/testing_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第52章\_zephyr\_\_bluetooth\_\_testing.h\_文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/testing_8h.html)。读取日期：2026-10-17；来源摘要见[来源记录](../SOURCES.md)。

蓝牙的内部测试接口（Internal Testing Interfaces）。

<a id="details"></a>

```c
#include <zephyr/net_buf.h>
```

查看此文件的源码。

蓝牙的内部测试接口（Internal Testing Interfaces）。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 52.1\_函数（Functions）

<a id="r_ad881c44e84d8ba4650a33ef6bae19c4c"></a>

```c
void bt_testing_trace_event_acl_pool_destroy (struct net_buf *buf)
```

相关声明：[bt_testing_trace_event_acl_pool_destroy](#ad881c44e84d8ba4650a33ef6bae19c4c)、[net_buf](../network_core_model_reference/P046_net_buf_结构体.md)。

`acl_in_pool.destroy` 的钩子（hook）。

<a id="r_a818681eaff28ef3f170c7329920e508d"></a>

```c
void bt_testing_trace_ext_adv_reassembly_timeout (void)
```

相关声明：[bt_testing_trace_ext_adv_reassembly_timeout](#a818681eaff28ef3f170c7329920e508d)。

跟踪扩展广播报告（extended advertising report）重组超时。

<a id="r_aa1b44cdccf5bdbae54334fef4859d886"></a>

```c
void bt_testing_trace_ext_adv_reassembly_complete (void)
```

相关声明：[bt_testing_trace_ext_adv_reassembly_complete](#aa1b44cdccf5bdbae54334fef4859d886)。

跟踪分片扩展广播报告的交付。

## 52.2\_详细说明（Detailed Documentation）

<a id="ad881c44e84d8ba4650a33ef6bae19c4c"></a>

### `bt_testing_trace_event_acl_pool_destroy()`

```c
void bt_testing_trace_event_acl_pool_destroy ( struct net_buf * buf)
```

`acl_in_pool.destroy` 的钩子（hook）。

弱函数接口（weak-function interface）。用户只需定义此函数，它就会自动成为事件侦听器（event listener）。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_BT_TESTING` 时可用。

<a id="aa1b44cdccf5bdbae54334fef4859d886"></a>

### `bt_testing_trace_ext_adv_reassembly_complete()`

```c
void bt_testing_trace_ext_adv_reassembly_complete ( void )
```

跟踪分片扩展广播报告的交付。

弱函数接口；分片扩展广播报告链完成全部重组并交付应用程序后调用。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_BT_TESTING` 时可用。

<a id="a818681eaff28ef3f170c7329920e508d"></a>

### `bt_testing_trace_ext_adv_reassembly_timeout()`

```c
void bt_testing_trace_ext_adv_reassembly_timeout ( void )
```

跟踪扩展广播报告（extended advertising report）重组超时。

弱函数接口；分片扩展广播报告链的主机重组定时器到期时调用。

**注意（Attention）**：注意：仅在启用 Kconfig 选项 `CONFIG_BT_TESTING` 时可用。


## 52.3\_原页交叉引用（Cross References）

- [zephyr/net_buf.h](../api_source_system_reference/P021_net_buf.h_源码浏览.md)
- [查看此文件的源码。](../api_source_reference/P862_testing.h_源码浏览.md)
- [net_buf](../network_core_model_reference/P046_net_buf_结构体.md)
- [CONFIG_BT_TESTING](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_BT_TESTING)

<a id="header-details"></a>
<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P051_____w__zephyr__zephyr__subsys__testsuite__include__zephyr__tc_util.h_文件参考.md) · [返回大纲](大纲.md) · [下一章](P053_zephyr__dt-bindings__sensor__tmp114.h_文件参考.md)
