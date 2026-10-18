---
id: learning.zephyr-docs.bluetooth.page-24
title: 蓝牙Mesh接口
kind: reference
status: maintained
domains: [zephyr, bluetooth, documentation]
source_url: https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="bluetooth-mesh-profile"></a>
<a id="bluetooth-mesh"></a>

# 第24章\_蓝牙Mesh接口

原文：[官方页面](https://docs.zephyrproject.org/latest/services/connectivity/bluetooth/api/mesh.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

蓝牙网状网络配置文件（Bluetooth Mesh Profile）为低功耗蓝牙（Bluetooth Low Energy）增加安全的无线多跳通信（Multi-hop Communication）。本模块实现 [蓝牙Mesh协议规范1.1.1版](https://www.bluetooth.com/specifications/specs/mesh-protocol-1-1-1/)。

更多Mesh信息见[蓝牙技术联盟（Bluetooth Special Interest Group，Bluetooth SIG）网站](https://www.bluetooth.com/bluetooth-resources/?tags=mesh)。

## 24.1\_官方章节入口

- [核心（Core）](P066_Mesh核心.md)。
- [访问层（Access layer）](P067_Mesh访问层.md)。
- [Mesh模型（Mesh models）](P068_Mesh模型.md)。
- [消息（Message）](P069_Mesh消息.md)。
- [分段与重组（Segmentation and Reassembly，SAR）](P095_Mesh分段与重组.md)。
- [配网（Provisioning）](P070_Mesh配网.md)。
- [代理（Proxy）](P071_Mesh代理.md)。
- [心跳（Heartbeat）](P072_Mesh心跳.md)。
- [运行时配置（Runtime Configuration）](P073_Mesh运行时配置.md)。
- [Mesh统计（Mesh Statistic）](P075_Mesh统计.md)。
- [蓝牙Mesh命令解释器（Bluetooth Mesh Shell）](P106_Mesh_Shell.md)。
- [子网桥接（Subnet Bridge）](P092_Mesh子网桥接.md)。
- [配置数据库（Configuration Database，CDB）](P074_Mesh配置数据库.md)。

> 译注：规范版本按本次读取的官方页面保留。该页是Mesh章节总入口，十三个子页按各自范围单独登记；入口翻译完成不代表协议实现或子页翻译已经全部完成。


对应官方文档源码：[doc/services/connectivity/bluetooth/api/mesh.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/services/connectivity/bluetooth/api/mesh.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/services/connectivity/bluetooth/api/mesh.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：蓝牙标准服务](P023_蓝牙标准服务.md) · [本模块主线目录](../reading/bluetooth.md) · [全部主线](../reading/README.md) · [下一篇：GAP_Shell](P025_GAP_Shell.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P023_蓝牙标准服务.md) · [返回大纲](大纲.md) · [下一章](P025_GAP_Shell.md)

</details>

<!-- reading-navigation:end -->
