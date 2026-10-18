---
id: learning.zephyr-docs.external_modules.page-25
title: LuDLC数据链路协议
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/ludlc.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="ludlc"></a>
<a id="external-module-ludlc"></a>

# 第25章\_LuDLC数据链路协议

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/ludlc.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 25.1\_简介（Introduction）

轻量微设备链路控制（Lightweight Micro Devices Link Control，LuDLC）是面向资源受限系统、独立于具体传输的数据链路协议（Data-link Protocol）。

它在UART、SPI或CAN总线等简单传输上提供可靠、有序的通信，无须完整网络协议栈。功能包括流控（Flow Control）、重传（Retransmission）、连接管理和通道复用（Channel Multiplexing），适合TCP/IP过重或不可用的场景。

LuDLC采用双重许可表达式 `Apache-2.0 OR GPL-2.0-or-later`。

<a id="usage-with-zephyr"></a>

## 25.2\_在Zephyr中使用（Usage with Zephyr）

将LuDLC以 `ludlc` 模块加入原文 `west.yaml` 的项目列表，或新建 `zephyr/submanifests/ludlc.yaml` 子清单，写入以下内容并运行 `west update`：

```yaml
manifest:
  projects:
    - name: ludlc
      url: https://github.com/avolkov-1221/ludlc.git
      revision: main
      path: modules/ludlc # adjust the path as needed
```

<a id="reference"></a>

## 25.3\_参考资料（Reference）

原页保留此标题但未另列条目；模块仓库地址见清单。


对应官方文档源码：[doc/develop/manifest/external/ludlc.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/ludlc.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/ludlc.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：libmpix图像处理](P024_libmpix图像处理.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：Thrift](P026_Thrift.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P024_libmpix图像处理.md) · [返回大纲](大纲.md) · [下一章](P026_Thrift.md)

</details>

<!-- reading-navigation:end -->
