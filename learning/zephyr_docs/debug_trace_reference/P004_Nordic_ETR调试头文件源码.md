---
id: learning.zephyr-docs.debug-trace-reference.page-4
title: Nordic_ETR调试头文件源码
kind: reference
status: maintained
domains: [zephyr, kernel, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/debug__nrf__etr_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第4章\_Nordic\_ETR调试头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/debug__nrf__etr_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；相关页面见[头文件参考](P003_Nordic_ETR调试头文件参考.md)和[公共接口](P003_Nordic_ETR调试头文件参考.md)；访问语义和生命周期见本页译注。

## 4.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="adebug__nrf__etr_8h_html_a697e26f514c888662c130c11e8793238"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2024 Nordic Semiconductor ASA
<a id="l00003"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00004"></a> */
<a id="l00005"></a>
<a id="l00006"></a>#ifndef _ZEPHYR_DRIVERS_DEBUG_CORESIGHT_NRF_ETR_H_
<a id="l00007"></a>#define _ZEPHYR_DRIVERS_DEBUG_CORESIGHT_NRF_ETR_H_
<a id="l00008"></a>
<a id="l00009"></a>#ifdef __cplusplus
<a id="l00010"></a>extern "C" {
<a id="l00011"></a>#endif
<a id="l00012"></a>
<a id="l00014"></a>void debug_nrf_etr_flush(void);
<a id="l00015"></a>
<a id="l00016"></a>#ifdef __cplusplus
<a id="l00017"></a>}
<a id="l00018"></a>#endif
<a id="l00019"></a>
<a id="l00020"></a>#endif /* _ZEPHYR_DRIVERS_DEBUG_CORESIGHT_NRF_ETR_H_ */
</code></pre>

## 4.2\_可见注释译文（Comments）

1. 版权与许可证：Copyright (c) 2024 Nordic Semiconductor ASA；SPDX-License-Identifier: Apache-2.0。原始法律声明保留。

2. _ZEPHYR_DRIVERS_DEBUG_CORESIGHT_NRF_ETR_H_头文件包含保护结束。

## 4.3\_原页符号提示（Symbol Descriptions）

### `debug_nrf_etr_flush`

```c
void debug_nrf_etr_flush(void)
```

刷新ETR缓冲区（ETR Buffer）中的数据。

符号定位：[debug_nrf_etr_flush](P003_Nordic_ETR调试头文件参考.md#a697e26f514c888662c130c11e8793238)。

## 4.4\_源码跟踪译注

> 译注——此接口属于官方Nordic ETR驱动。当前实现按配置初始化解码器，将输出切换为阻塞轮询（Blocking Polling），在中断锁定期间调用四次process(false)，然后恢复中断。函数返回void，并忽略内部处理返回值；不能从调用返回推断下游设备已确认接收。

> 译注——当前flush设置use_blocking为true后不在此函数内恢复异步输出模式。这是所核对版本的实现行为；应用是否需要主动调用，应结合目标平台、配置和驱动整体流程判断。

头文件定位：[include/zephyr/drivers/debug/debug_nrf_etr.h](../../../include/zephyr/drivers/debug/debug_nrf_etr.h)，关联实现／接口：[drivers/debug/debug_nrf_etr.c](../../../drivers/debug/debug_nrf_etr.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/debug/debug_nrf_etr.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/debug/debug_nrf_etr.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未构建固件、配置实板引脚或操作硬件。

## 4.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](P003_Nordic_ETR调试头文件参考.md)
- [debug_nrf_etr_flush](P003_Nordic_ETR调试头文件参考.md#a697e26f514c888662c130c11e8793238)

---

[上一章](P003_Nordic_ETR调试头文件参考.md) · [返回大纲](大纲.md)
