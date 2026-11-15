---
id: learning.zephyr-docs.memory-retention-reference.page-6
title: Nordic保留内存头文件源码
kind: reference
status: maintained
domains: [zephyr, storage, source, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/nrf__retained__mem_8h_source.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第6章\_Nordic保留内存头文件源码

原文：[官方源码浏览页](https://docs.zephyrproject.org/latest/doxygen/html/nrf__retained__mem_8h_source.html)。读取日期：2026-10-15；摘要见[来源记录](../SOURCES.md)。

本页保留官方Doxygen源码浏览页的全部可见代码及注释，移除展示行号、还原不换行空格并清除行尾空白。代码、标识符与许可证不翻译替换，中文对照列在后面。原网页隐藏了部分API文档注释，所以原始行号会跳跃；完整接口说明见[头文件参考](../hardware/P634_Nordic保留内存头文件.md)和[公共API](../hardware/P634_Nordic保留内存头文件.md)。

## 6.1\_原始可见代码（Source Code）

原始行号锚点保留在对应代码行，使用Markdown内嵌HTML预格式代码容器承载。

<a id="agroup__system__errno_html_ga91457bbf35f0f1085619a99423bb1f33"></a>
<a id="aretained__mem_8h_html"></a>

<pre><code class="language-c"><a id="l00001"></a>/*
<a id="l00002"></a> * Copyright (c) 2024 Nordic Semiconductor ASA
<a id="l00003"></a> *
<a id="l00004"></a> * SPDX-License-Identifier: Apache-2.0
<a id="l00005"></a> */
<a id="l00006"></a>
<a id="l00007"></a>#ifndef ZEPHYR_INCLUDE_DRIVERS_RETAINED_MEM_NRF_RETAINED_MEM_H
<a id="l00008"></a>#define ZEPHYR_INCLUDE_DRIVERS_RETAINED_MEM_NRF_RETAINED_MEM_H
<a id="l00009"></a>
<a id="l00010"></a>#ifdef __cplusplus
<a id="l00011"></a>extern "C" {
<a id="l00012"></a>#endif
<a id="l00013"></a>
<a id="l00014"></a>#include &lt;zephyr/drivers/retained_mem.h&gt;
<a id="l00015"></a>
<a id="l00016"></a>#if defined(CONFIG_RETAINED_MEM_NRF_RAM_CTRL) || defined(__DOXYGEN__)
<a id="l00025"></a>int z_nrf_retained_mem_retention_apply(void);
<a id="l00026"></a>#else
<a id="l00027"></a>static inline int z_nrf_retained_mem_retention_apply(void)
<a id="l00028"></a>{
<a id="l00029"></a>        return -ENOTSUP;
<a id="l00030"></a>}
<a id="l00031"></a>#endif
<a id="l00032"></a>
<a id="l00033"></a>#ifdef __cplusplus
<a id="l00034"></a>}
<a id="l00035"></a>#endif
<a id="l00036"></a>
<a id="l00037"></a>#endif /* ZEPHYR_INCLUDE_DRIVERS_RETAINED_MEM_NRF_RETAINED_MEM_H */
</code></pre>

## 6.2\_可见注释译文（Comments）

1. 版权：Copyright (c) 2024 Nordic Semiconductor ASA。Apache-2.0许可证原文保留。

2. 结束头文件包含保护ZEPHYR_INCLUDE_DRIVERS_RETAINED_MEM_NRF_RETAINED_MEM_H。

## 6.3\_原页符号提示（Symbol Descriptions）

### `ENOTSUP`

```c
#define ENOTSUP
```

不支持的值（Unsupported Value）。

定义位置（Definition）：errno.h:115。

符号定位：[ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)。

### `retained_mem.h`

保留内存驱动API的主头文件。

符号定位：[retained_mem.h](../hardware/P633_保留内存头文件.md)。

## 6.4\_源码跟踪译注

> 译注——官方平台专用内容：这是Zephyr官方Nordic保留内存扩展头文件，不是本仓库自行添加的芯片资料，也不表示HC32支持这一平台接口。功能是按设备树配置应用RAM保留设置，不是保存应用数据或校验内容。

> 译注——条件分支：启用CONFIG_RETAINED_MEM_NRF_RAM_CTRL时声明外部实现；__DOXYGEN__使文档生成能看到同一声明，不是应用功能开关。未启用配置时内联后备实现直接返回-ENOTSUP。头文件文档约定成功0、无保留配置-ENOTSUP、设置失败-EIO。

> 译注——实现差异：当前关联实现遍历状态为okay的zephyr_retained_ram节点，并取其父节点的地址／大小。TF-M安全服务分支中某一区域设置失败会记录-EIO，但继续处理其余区域；因此失败不保证前面未生效。普通nrfx分支直接调用设置函数。该外部实现自身没有空列表返回-ENOTSUP的检查；若生成空列表且该实现仍被编译，循环不执行并返回初始0。与头文件的概括约定分开陈述，未声称已验证这类构建组合。

头文件相对定位：[include/zephyr/drivers/retained_mem/nrf_retained_mem.h](../../../include/zephyr/drivers/retained_mem/nrf_retained_mem.h)，关联实现／接口：[drivers/retained_mem/retained_mem_nrf_ram_ctrl.c](../../../drivers/retained_mem/retained_mem_nrf_ram_ctrl.c)；[官方原始头文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/include/zephyr/drivers/retained_mem/nrf_retained_mem.h)与[官方关联文件](https://github.com/zephyrproject-rtos/zephyr/blob/main/drivers/retained_mem/retained_mem_nrf_ram_ctrl.c)的摘要见来源记录。去掉注释和展示空白后，本页代码与本次读取的原始头文件一致，不能推广到以后滚动更新的main或任意本地版本。

本次验证范围为文档与源码对照，未编译或执行存储写入、掉电、低功耗、非法参数及实板实验。

## 6.5\_原页交叉引用（Cross References）

- [查看此文件参考说明](../hardware/P634_Nordic保留内存头文件.md)
- [zephyr/drivers/retained_mem.h](../hardware/P633_保留内存头文件.md)
- [ENOTSUP](../error_reference/P003_系统错误号公共接口.md#ga91457bbf35f0f1085619a99423bb1f33)

---

[上一章](P005_数据保留服务头文件源码.md) · [返回大纲](大纲.md)
