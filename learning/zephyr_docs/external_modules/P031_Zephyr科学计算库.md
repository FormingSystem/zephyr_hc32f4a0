---
id: learning.zephyr-docs.external_modules.page-31
title: Zephyr科学计算库
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/zscilib.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="zephyr-scientific-library-zscilib"></a>
<a id="external-module-zscilib"></a>

# 第31章\_Zephyr科学计算库

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/zscilib.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 31.1\_简介（Introduction）

[Zephyr科学计算库（Zephyr Scientific Library，zscilib）](https://github.com/zephyrproject-rtos/zscilib)旨在为资源受限嵌入式设备提供科学计算（Scientific Computing）、数据分析和数据处理函数。

库完全用C编写。主要开发目标是Zephyr，同时尽可能保持可移植性；随附独立参考工程，可在非Zephyr项目使用。

<a id="usage-with-zephyr"></a>

## 31.2\_在Zephyr中使用（Usage with Zephyr）

在原文 `west.yaml` 中添加项目，或新建 `zephyr/submanifests/zscilib.yaml` 子清单，写入以下内容后运行 `west update`：

```yaml
manifest:
  projects:
    - name: zscilib-
      url: https://github.com/zephyrproject-rtos/zscilib
      revision: master
      path: modules/lib/zscilib # adjust the path as needed
```

> 译注——项目名称：原例name为带尾部连字符的 `zscilib-`，而path为 `modules/lib/zscilib`；两者职责不同。按原例使用定向west命令时，项目选择应与实际清单name一致，不能仅根据目录名猜测。

详细操作及API见 [zscilib文档](https://zephyrproject-rtos.github.io/zscilib/)和 [示例](https://github.com/zephyrproject-rtos/zscilib/tree/master/samples)。

<a id="running-a-sample-application"></a>

### 31.2.1\_运行示例应用（Running a sample application）

使用QEMU运行示例：

```text
$ west build -p -b qemu_cortex_a53 \
    samples/matrix/mult -t run
...
*** Booting Zephyr OS build zephyr-v2.6.0-536-g89212a7fbf5f  ***
zscilib matrix mult demo


mtx multiply output (4x3 * 3x4 = 4x4):

14.000000 17.000000 20.000000 23.000000
35.000000 44.000000 53.000000 62.000000
56.000000 71.000000 86.000000 101.000000
7.000000 9.000000 11.000000 13.000000
```

按CTRL+A，再按x退出QEMU。

> 译注——位置和输出：`samples/matrix/mult` 相对于zscilib模块根目录，执行前进入该目录；`$`是提示符。matrix mult demo表示矩阵乘法演示，原输出计算4×3与3×4矩阵相乘得到4×4结果。历史Zephyr版本与矩阵数值按原文保留，不是本批测试结果。

<a id="running-unit-tests"></a>

### 31.2.2\_运行单元测试（Running Unit Tests）

运行库的单元测试（Unit Test）：

```text
$ west twister --inline-logs -p mps2/an521/cpu0 -T tests
See the tests folder for further details.
```

> 译注：同样以zscilib模块根为当前位置，`-T tests` 指模块的测试目录。末行“See the tests folder for further details.”是“更多细节见tests目录”的说明，不是Shell命令。

<a id="reference"></a>

## 31.3\_参考资料（Reference）

原页保留此标题，未在下面另列条目。


对应官方文档源码：[doc/develop/manifest/external/zscilib.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/zscilib.rst)。

> 译注——源码跟踪：本仓库的[对应源码](../../../doc/develop/manifest/external/zscilib.rst)可用于跟踪，版本可能与网页不同；本批仅翻译和核对文档，没有执行固件构建、模拟运行或烧录。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：Zephelin性能分析](P030_Zephelin性能分析.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：ZView运行时可视化](P032_ZView运行时可视化.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P030_Zephelin性能分析.md) · [返回大纲](大纲.md) · [下一章](P032_ZView运行时可视化.md)

</details>

<!-- reading-navigation:end -->
