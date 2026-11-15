---
id: learning.zephyr-docs.linker-reference.page-13
title: 链接器devnull区域头文件参考
kind: reference
status: maintained
domains: [zephyr, hardware, api]
source_url: https://docs.zephyrproject.org/latest/doxygen/html/linker-devnull_8h.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

# 第13章\_链接器devnull区域头文件参考

原文：[官方页面](https://docs.zephyrproject.org/latest/doxygen/html/linker-devnull_8h.html)。读取日期：2026-10-15；来源摘要见[来源记录](../SOURCES.md)。

> 译注——阅读位置：从[本册大纲](大纲.md)区分设备树区域生成、工具链适配、只读检测与链接符号。源码跟踪译注与官方原文分开标示。

查看此文件的源码。

## 13.1\_源码定位与版本边界

相对源码定位：[设备树区域](../../../include/zephyr/linker/devicetree_regions.h)、[只读检测](../../../include/zephyr/linker/utils.h)、[适配选择](../../../include/zephyr/linker/linker-tool.h)、[GCC](../../../include/zephyr/linker/linker-tool-gcc.h)、[LLD](../../../include/zephyr/linker/linker-tool-lld.h)、[MWDT](../../../include/zephyr/linker/linker-tool-mwdt.h)、[devnull](../../../include/zephyr/linker/linker-devnull.h)、[链接符号](../../../include/zephyr/linker/linker-defs.h)、[区域绑定](../../../dts/bindings/base/zephyr,memory-region.yaml)、[LLD构建入口](../../../cmake/linker/lld/target.cmake)、[LLD标志](../../../cmake/linker/lld/linker_flags.cmake)、[通用LD标志](../../../cmake/linker/ld/linker_flags.cmake)、[日志段](../../../include/zephyr/linker/common-rom/common-rom-logging.ld)、[内存管理](../../../include/zephyr/kernel/mm.h)和[虚拟内核条件](../../../include/zephyr/kernel/internal/mm.h)。本次官方源码摘要见[来源记录](../SOURCES.md)。

> 译注——源码核对：保留ELF、排除二进制：devnull是链接时用于特定段的虚拟区域名称，不是操作系统的/dev/null，也不是将内容从ELF彻底删除。common-rom-logging.ld在CONFIG_LOG_FMT_SECTION_STRIP且DEVNULL_REGION存在时，把相应日志段标为COPY并放入DEVNULL_REGION；这与/DISCARD/不同，仍需下游镜像生成规则配合。

> 译注——源码核对：条件与位置：此头文件只在CONFIG_LINKER_DEVNULL_MEMORY启用时提供区域常量。XIP分支尝试将区域放到ROM之后，否则放到ROM之前，不能满足条件时#error；非XIP分支按RAM_ADDR与DEVNULL_SIZE关系选择RAM之前或之后。原长注释主要描述ROM情形，不能忽略非XIP分支。未定义ROM／RAM地址、基址或大小时按相应条件报错；区域常量不会保留真实硬件容量。

> 译注——源码核对：版本边界：本批记录八份链接器头文件、设备树绑定、三份链接器CMake文件、日志链接片段及两份内存管理头文件，共十五份官方源码摘要。八个源码浏览页的非注释代码与本次读取的原始头文件逐项核对；滚动main、latest与本仓库参照版本不自动等同。本次未预处理或链接示例、构建固件、配置内存权限或执行硬件实验。

本次验证范围为文档与源码对照，未编译宏／DTS示例、构建固件或操作硬件。

## 13.2\_原页交叉引用（Cross References）

- [查看此文件的源码](P014_链接器devnull区域头文件源码.md)

---

[上一章](P012_MWDT链接器适配头文件源码.md) · [返回大纲](大纲.md) · [下一章](P014_链接器devnull区域头文件源码.md)
