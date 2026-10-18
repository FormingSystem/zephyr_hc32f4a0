---
id: learning.zephyr-docs.external_modules.page-23
title: 工业IO库libiio
kind: reference
status: maintained
domains: [zephyr, external_modules, documentation]
source_url: https://docs.zephyrproject.org/latest/develop/manifest/external/libiio.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航和明确标注的译注为本地新增。 -->

<a id="libiio"></a>
<a id="external-module-libiio"></a>

# 第23章\_工业IO库libiio

原文：[官方页面](https://docs.zephyrproject.org/latest/develop/manifest/external/libiio.html)。读取日期：2026-10-14；保存的 latest 页面及 HTML 摘要见[来源记录](../SOURCES.md)。

> 译注——接入前提：本页是Zephyr官网列出的外部模块介绍。清单片段应合并到读者工作区的实际活动清单；原文部分页面称 `west.yaml`，Zephyr上游默认文件名为 `west.yml`。子清单只有被活动清单导入时才会生效；[官方west.yml](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/west.yml)以 `self.import: submanifests` 导入示例目录。不要仅为照抄文件名另建未被读取的清单或替换既有清单。

> 译注——操作与许可：YAML、头文件包含及Kconfig片段是写入对应文件的内容；west命令从读者已配置工具、Python环境和west的工作区执行，路径均按该工作区解析。更新依赖、安装工具、构建和实机验证是不同步骤；本批没有执行这些操作。外部组件许可证按各页原文分别保留，翻译文档的许可证不替代组件许可。

<a id="introduction"></a>

## 23.1\_简介（Introduction）

<a id="id3"></a>

[libiio](https://github.com/analogdevicesinc/libiio) 主要由Analog Devices开发，是访问Linux工业输入输出（Industrial Input/Output，IIO）设备的开源库，覆盖模数转换器（Analog-to-Digital Converter，ADC）、数模转换器（Digital-to-Analog Converter，DAC）、加速度计、陀螺仪、惯性测量单元（Inertial Measurement Unit，IMU）、压力／温度传感器及射频（Radio Frequency，RF）收发器等。它可在目标本机运行，也可让Linux、Windows或macOS主机通过USB、以太网或串口远程访问目标。

<a id="id7"></a>

<a id="id5"></a>

仓库包含Zephyr模块，可把应用变成这样的远程目标。IIO设备和通道接入Zephyr设备模型，内置驱动适配现有传感器及ADC／DAC驱动；IIO守护进程（Daemon）iiod的Zephyr移植通过网络套接字、UART控制台、USB CDC-ACM或原生USB厂商类开放设备。现有libiio Python绑定、`iio_info` 等命令行工具和 [Scopy](https://analogdevicesinc.github.io/scopy) 桌面应用，可从上述主机系统直接访问Zephyr目标，无须修改。详情见 [Zephyr移植文档](https://analogdevicesinc.github.io/libiio/main/zephyr/)。

核心库采用GNU宽通用公共许可证（GNU Lesser General Public License，LGPL）2.1，示例／测试应用采用GNU通用公共许可证（GNU General Public License，GPL）2.0。上述Zephyr集成及其静态链接的核心文件采用MIT许可证。

<a id="usage-with-zephyr"></a>

## 23.2\_在Zephyr中使用（Usage with Zephyr）

在 `west.yml` 中添加项目，或新建 `zephyr/submanifests/libiio.yaml` 子清单，写入以下内容并运行 `west update`：

```yaml
manifest:
  remotes:
    - name: analogdevicesinc
      url-base: https://github.com/analogdevicesinc

  projects:
    - name: libiio
      remote: analogdevicesinc
      revision: main
      path: modules/lib/libiio
```

<a id="reference"></a>

## 23.3\_参考资料（Reference）


<a id="id2"></a>

1. [libiio仓库](https://github.com/analogdevicesinc/libiio)。

<a id="id4"></a>

2. [Zephyr移植文档](https://analogdevicesinc.github.io/libiio/main/zephyr/)。

<a id="id6"></a>

3. [Scopy](https://analogdevicesinc.github.io/scopy)。


对应官方文档源码：[doc/develop/manifest/external/libiio.rst](https://raw.githubusercontent.com/zephyrproject-rtos/zephyr/main/doc/develop/manifest/external/libiio.rst)。

> 译注——源码版本：本仓库参照版本尚无该文档，请按上方官方来源跟踪相应版本；本批仅翻译和核对文档。

<!-- reading-navigation:start -->

**主线阅读**

[上一篇：立方星空间协议libcsp](P022_立方星空间协议libcsp.md) · [本模块主线目录](../reading/external_modules.md) · [全部主线](../reading/README.md) · [下一篇：libmpix图像处理](P024_libmpix图像处理.md)

<details>
<summary>原册编号导航（含扩展参考）</summary>

[上一章](P022_立方星空间协议libcsp.md) · [返回大纲](大纲.md) · [下一章](P024_libmpix图像处理.md)

</details>

<!-- reading-navigation:end -->
