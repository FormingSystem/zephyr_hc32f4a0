---
id: learning.zephyr-docs.debug-trace-reference.page-3
title: Nordic_ETR调试头文件参考
kind: reference
status: maintained
domains: [zephyr, kernel, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/debug__nrf__etr_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第3章\_Nordic\_ETR调试头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/debug__nrf__etr_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)进入调试服务目录、CoreSight解格式器源码与Nordic ETR接口。源码跟踪译注与官方原文分开标示。

查看此文件的源码。

<a id="header-func-members"></a>
<a id="func-members"></a>

## 3.1\_函数（Functions）

<a id="r_a697e26f514c888662c130c11e8793238"></a>

```c
void debug_nrf_etr_flush (void)
```

相关声明：[debug_nrf_etr_flush](#a697e26f514c888662c130c11e8793238)。

刷新ETR缓冲区（ETR Buffer）中的数据。

## 3.2\_详细说明（Detailed Documentation）

<a id="a697e26f514c888662c130c11e8793238"></a>

### `debug_nrf_etr_flush()`

```c
void debug_nrf_etr_flush ( void )
```

刷新ETR缓冲区（ETR Buffer）中的数据。

## 3.3\_源码定位与版本边界

源码定位：[include/zephyr/drivers/debug/debug_nrf_etr.h](../../../include/zephyr/drivers/debug/debug_nrf_etr.h)、[drivers/debug/debug_nrf_etr.c](../../../drivers/debug/debug_nrf_etr.c)。官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：以下源码跟踪译注独立于官方正文，依据来源记录中保存摘要的官方main文件。

> 译注——源码核对：此接口属于官方Nordic ETR驱动。当前实现按配置初始化解码器，将输出切换为阻塞轮询（Blocking Polling），在中断锁定期间调用四次process(false)，然后恢复中断。函数返回void，并忽略内部处理返回值；不能从调用返回推断下游设备已确认接收。

> 译注——源码核对：当前flush设置use_blocking为true后不在此函数内恢复异步输出模式。这是所核对版本的实现行为；应用是否需要主动调用，应结合目标平台、配置和驱动整体流程判断。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 3.4\_原页交叉引用（Cross References）

- [查看此文件的源码](P004_Nordic_ETR调试头文件源码.md)

<a id="doc-func-members"></a>
<a id="header-doc-func-members"></a>

---

[上一章](P002_CoreSight跟踪解格式头文件源码.md) · [返回大纲](大纲.md) · [下一章](P004_Nordic_ETR调试头文件源码.md)
