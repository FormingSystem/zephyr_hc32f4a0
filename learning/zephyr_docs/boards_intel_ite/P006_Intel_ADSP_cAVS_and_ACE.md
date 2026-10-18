---
id: learning.zephyr-docs.boards-intel-ite.page-6
title: Intel ADSP cAVS and ACE
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/intel/adsp/doc/intel_adsp_generic.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="intel-adsp-cavs-and-ace"></a>

<a id="intel-adsp-generic"></a>

# 第6章\_Intel ADSP cAVS与ACE

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/intel/adsp/doc/intel_adsp_generic.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

Intel音频及数字信号处理（ADSP / Audio and Digital Signal Processing）硬件包括融合音频语音（cAVS / Converged Audio Voice Speech）系列，以及后继的音频与上下文引擎（ACE / Audio and Context Engine）。这些基于Xtensa的ADSP可集成到多种Intel产品中。下表列出各版Intel ADSP兼容的部分Intel微处理器。

<table>
<tr>
<th>音频数字信号处理器（ADSP）</th>
<th>微处理器（Microprocessor）</th>
</tr>
<tr>
<td>cAVS 1.5</td>
<td>Apollo Lake</td>
</tr>
<tr>
<td>cAVS 1.8</td>
<td>Whiskey Lake</td>
</tr>
<tr>
<td>cAVS 2.5</td>
<td>Tiger Lake</td>
</tr>
<tr>
<td>ACE 1.5</td>
<td>Meteor Lake</td>
</tr>
</table>

Intel通过Sound Open Firmware（[SOF](https://thesofproject.github.io/latest/index.html)）项目开源其ADSP硬件固件。SOF既可基于Zephyr构建，也可基于Cadence专有Xtensa操作系统（XTOS）构建，并在多种Intel及非Intel平台运行。

Intel [UP Xtreme](https://up-board.org/up-xtreme/)产品线提供公开可获得的参考板，用于Zephyr的Intel ADSP支持。本指南以[UP Xtreme i11-0001系列](https://up-shop.org/up-xtreme-i11-boards-0001-series.html)开发板，即[Intel ADSP CAVS 2.5](P005_Intel_ADSP_CAVS_2.5.md#intel-adsp-cavs25)，为例。除特别说明外，以下步骤具有通用性，也适用于其他开发板；涉及特定开发板时会引导查阅相应文档。

<a id="system-requirements"></a>

## 系统要求（System Requirements）

<a id="setting-up-target-board"></a>

### 设置目标开发板（Target Board）

向ADSP烧录Zephyr必须使用Zephyr的Python工具，该工具运行于开发板主CPU上的Linux主机。用户可以、且原文建议在开发计算机上构建二进制文件，再远程烧录；但开发板本身必须能够运行Python脚本，接收West通过网络发送的二进制文件并烧录。应安装支持或附带Zephyr所需Python版本的Linux。原文建议考虑自带Python 3.8的Ubuntu 20.04。

如果计划在开发板上使用SOF，需要构建并安装修改后的Linux SOF内核，替换默认内核。建议按SOF说明在Zephyr上构建和运行SOF。（[SOF说明（Instructions）](https://thesofproject.github.io/latest/getting_started/build-guide/build-with-zephyr.html)）

UP Xtreme用户可参考UP Community维基，了解在开发板上安装Linux的方法。（[UP Community维基（Wiki）](https://github.com/up-board/up-community/wiki/Ubuntu)）

<a id="signing-tool"></a>

### 签名工具（Signing Tool）

从Skylake起，Intel产品强制要求固件二进制文件签名，因此还需准备SOF rimage签名工具及密钥。

```text
git clone https://github.com/thesofproject/rimage
git submodule update --init
cd tools/rimage/
```

按rimage README.md说明在系统上构建工具。可将可执行文件复制到PATH中的目录，或执行`west config rimage.path /path/to/rimage-build/rimage`；更多细节见`west sign -h`输出。直接从构建目录运行可降低误用旧版rimage的可能。

平台专用配置位于`rimage/config/`子目录。若使用其他配置目录，可执行`west config build.cmake-args -- -DRIMAGE_CONFIG_PATH=/path/to/my/rimage/config`。

<a id="xtensa-toolchain-optional"></a>

### Xtensa工具链，可选（Optional）

Zephyr SDK提供基于GCC的工具链，可为cAVS及ACE开发板构建Zephyr。若需要更高优化程度，也可使用[Cadence](https://www.cadence.com/en_US/home/tools/ip/tensilica-ip.html)提供的专有Xtensa工具链。以下说明假设用户已按照供应方要求，购买并安装适用于开发板的工具链及内核支持。

首先按Cadence要求设置`$HOME/.flexlmrc`文件或`XTENSAD_LICENSE_FILE`变量，然后设置以下环境变量：

```text
export XTENSA_TOOLCHAIN_PATH=$HOME/xtensa/XtDevTools/install/tools
export XTENSA_BUILDS_DIR=$XTENSA_TOOLCHAIN_PATH/../builds
export ZEPHYR_TOOLCHAIN_VARIANT=xcc
export TOOLCHAIN_VER=RG-2017.8-linux
export XTENSA_CORE=cavs2x_LX6HiFi3_2017_8
```

最后三个变量与cAVS／ACE版本有关，其值见对应开发板文档。

<a id="programming-and-debugging"></a>

## 烧录与调试（Programming and Debugging）

<a id="building"></a>

### 构建（Building）

按通常方式构建。

```text
# From the root of the zephyr repository
west build -b intel_adsp/cavs25 samples/hello_world
```

<a id="signing"></a>

### 签名（Signing）

`west build`会在构建结束时尝试为二进制文件签名。如需自行签名，可直接调用`west sign`。从west日志中找出`west sign`调用，可复制并修改该命令。更多细节见`west sign -h`。

构建流程尽量提供默认rimage参数。如需覆盖，可按具体情况选择不同方法。这些方法通常并不互斥，但为避免依赖未记录的rimage优先级规则，最好一次只使用一种。


- 本地交互使用优先采用west config中的`rimage.extra-args`，详见`west sign -h`。必要时可通过`WEST_CONFIG_LOCAL`环境变量指向其他west配置文件。
- 可在`rimage/config/`目录中新增或覆盖`$platform.toml`文件。
- 开发板专用需求可在`boards/my/board/board.cmake`中定义`WEST_SIGN_OPTS`，示例见`soc/intel/adsp/common/CMakeLists.txt`。

从Zephyr 3.6.0开始，`west flash`不再调用`west sign`，也不再接受rimage参数。构建二进制文件后，运行以下命令可查看Intel ADSP运行工具（Runner）的最新参数列表：

```text
west flash --context
```

<a id="remote-flashing-to-cavs-based-adsp"></a>

### 远程烧录基于cAVS的ADSP（Remote Flashing）

如前所述，建议远程运行并监视cAVS开发板上的Zephyr输出。ADSP烧录或运行出错时，主CPU上的Linux主机可能死机，需要重启。以下将开发板称为远程主机（Remote Host），开发计算机称为本地主机（Local Host）。

将以下脚本复制到cAVS开发板。[soc/intel/intel_adsp/tools/remote-fw-service.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/tools/remote-fw-service.py)接收West通过网络发送的二进制文件，再调用[soc/intel/intel_adsp/tools/cavstool.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/tools/cavstool.py)，下文称cAVS工具，由其烧录并采集日志。启动`remote-fw-service.py`。

```text
scp -r $ZEPHYR_BASE/soc/intel/intel_adsp/tools/cavstool.py username@remotehostname
scp -r $ZEPHYR_BASE/soc/intel/intel_adsp/tools/remote-fw-service.py username@remotehostname
ssh username@remotehostname
sudo ./remote-fw-service.py
```

`remote-fw-service.py`使用远程主机的9999及10000端口通信：9999为日志端口（Log Port），转发cavstool.py采集的日志；10000为请求端口（Requests Port），处理请求。本地主机运行West或Twister时，通过[soc/intel/intel_adsp/tools/cavstool_client.py](https://github.com/zephyrproject-rtos/zephyr/blob/main/soc/intel/intel_adsp/tools/cavstool_client.py)，即cAVS工具客户端，发送请求。它也使用本地主机的9999及10000端口，应确保端口空闲。

使用West烧录很简单：

```text
west flash --remote-host remotehostname --pty remotehostname
```

通过Twister运行测试稍复杂一些：

```text
twister -p intel_adsp/cavs25 --device-testing --device-serial-pty="$ZEPHYR_BASE/soc/intel/intel_adsp/tools/cavstool_client.py,-s,remotehostname,-l" --west-flash="--remote-host=remotehostname" -T samples/hello_world
```

如果网络将cavstool_client.py到remote-fw-service.py的TCP连接经中间主机转发，可能需要指定不同主机名及端口。可将端口号附加在中间主机名之后。

```text
west flash --remote-host intermediatehost:reqport --pty remotehostname:logport
twister -p intel_adsp/cavs25 --device-testing --device-serial-pty="$ZEPHYR_BASE/soc/intel/intel_adsp/tools/cavstool_client.py,-s,remotehostname:logport,-l" --west-flash="--remote-host=remotehostname:reqport" -T samples/hello_world
```

也可将这些信息保存为硬件映射文件（Hardware Map），传给Twister。

```text
twister -p intel_adsp/cavs25 --hardware-map cavs.map --device-testing -T samples/hello_world
```

cavs.map示例如下：

```text
- connected: true
  id: None
  platform: intel_adsp/cavs25
  product: None
  runner: intel_adsp
  serial_pty: "/home/zephyrus/zephyrproject/zephyr/soc/intel/intel_adsp/tools/cavstool_client.py,-s,remotehostname:logport,-l"
  runner_params:
  - --remote-host=remotehostname:reqport
```

通常传给Twister或West的参数都可通过硬件映射提供。如前所述，使用West烧录时传入`--context`，可查看Intel ADSP运行工具参数。

硬件映射详情见[测试运行工具（Test Runner / Twister）](../twister/P001_Twister测试运行器.md#twister-script)。

<a id="local-flashing-to-cavs-based-adsp"></a>

### 本地烧录基于cAVS的ADSP（Local Flashing）

也可在开发板上直接通过cAVS工具烧录已签名二进制文件，这有助于调试。

```text
sudo ./cavstool.py zephyr.ri
```

成功时，日志末尾应显示以下内容：

```text
***** Booting Zephyr OS vx.x.x-xxx-gxxxxxxxxxxxx *****
Hello World! intel_adsp
```

<a id="flashing-to-ace-based-adsp"></a>

### 烧录基于ACE的ADSP

原文说明，基于ACE ADSP的平台尚未公开提供，因此尚不支持烧录。

<a id="debugging"></a>

### 调试（Debugging）

Zephyr当时尚未为Intel ADSP平台支持GDB，原文建议使用Zephyr内置的[核心转储（Core Dump）](https://docs.zephyrproject.org/latest/services/debugging/coredump.html#coredump)及[日志（Logging）](../observability/P001_日志.md#logging-api)功能。

<a id="troubleshooting"></a>

## 故障排查（Troubleshooting）

可直接向Intel ADSP脚本传递详细输出选项（Verbose Flags）：

```text
sudo ./remote-fw-service.py -v
sudo ./cavstool.py zephyr.ri -v
```

查看参数列表：

```text
sudo ./remote-fw-service.py --help
sudo ./cavstool.py --help
```

如果在west sign阶段因无法解析密钥而烧录失败，可尝试重新安装最新版签名工具，例如：

```text
error: 1 unparsed keys left in 'adsp'
error: 1 unparsed arrays left in 'adsp'
```

在开发板上启动remote-fw-service.py时报“Address already in use”，可能已有另一个脚本实例运行，应终止该实例。

```text
$ sudo netstat -peanut | grep 9999
tcp   0   0 0.0.0.0:9999   0.0.0.0:*   LISTEN   0   289788   14795/python3
$ sudo kill 14795
```

如果West或Twister成功签名并与remote-fw-service.py建立TCP连接，却随后挂起且没有输出，可能是remote-fw-service.py通信失败，或cavstool.py烧录失败。登录远程主机，检查remote-fw-service.py输出。

出现“incorrect communication”提示，说明命令或硬件映射中混淆了日志及请求端口号，交换两者后重试。

```text
ERROR:remote-fw:incorrect monitor communication!
```

出现“load failed”提示，说明烧录失败。应检查`west flash`日志，并仔细核对`west sign`参数。

```text
WARNING:cavs-fw:Load failed?  FW_STATUS = 0x81000012
INFO:cavs-fw:cAVS firmware load complete
--
```

烧录失败或网络通信异常有时会破坏ADSP或remote-fw-service.py状态。如果反复失败且找不到原因，可重启脚本，或给开发板断电重启，以恢复状态。

用户，尤其是Xtensa工具链用户，也应考虑清理Zephyr缓存，因为偶尔会出现缓存问题。删除缓存及有关构建目录后重新开始；也可先尝试West的pristine选项。

```text
rm -rf build twister-out*
rm -rf ~/.ccache ~/.cache/zephyr
```

Xtensa工具链用户可通过导出`FLEXLM_DIAGNOSTICS=3`，获取更详细的许可证服务器日志。

## 译注

原文中的Ubuntu 20.04／Python 3.8建议、ACE尚未公开与不支持烧录、GDB支持状态及旧soc/intel/intel_adsp脚本路径均按来源记录，不作为当前环境实测结论。Zephyr 3.6.0之后west flash与west sign的职责变化也完整保留。

## 原文外链核对

2026-10-16核对并重试以下原文外链时未能确认可访问性，保留原始目标，不将访问失败解释为原文内容有误。

- [build-with-zephyr.html](https://thesofproject.github.io/latest/getting_started/build-guide/build-with-zephyr.html)：HTTP Error 404: Not Found。
- [up-xtreme-i11-boards-0001-series.html](https://up-shop.org/up-xtreme-i11-boards-0001-series.html)：HTTP Error 403: Forbidden。
- [tensilica-ip.html](https://www.cadence.com/en_US/home/tools/ip/tensilica-ip.html)：HTTP Error 403: Forbidden。

---

[上一章](P005_Intel_ADSP_CAVS_2.5.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P007_Bartlett_Lake_P_CRB.md)
