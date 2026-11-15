---
id: learning.zephyr-docs.firmware_update.mgmtex-updatehub
title: UpdateHub升级示例
kind: reference
status: maintained
domains: [zephyr, firmware_update]
source_url: https://docs.zephyrproject.org/latest/samples/subsys/mgmt/updatehub/README.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；阅读编号、导航和译注为本地新增。 -->

<a id="updatehub-fota"></a>

# 第25章\_UpdateHub升级示例

原文：[UpdateHub embedded Firmware Over-The-Air (FOTA) update](https://docs.zephyrproject.org/latest/samples/subsys/mgmt/updatehub/README.html)。读取日期：2026-10-13，`latest`。

## 25.1\_UpdateHub与运行模式

UpdateHub是面向嵌入式设备远程升级的服务，提供 **空中固件升级（Firmware Over-The-Air，FOTA）**的传输和管理功能。原文将其描述为企业级方案，强调安全与效率；更多说明见[UpdateHub文档](https://docs.updatehub.io/)。

示例有两种模式。**轮询模式（Polling Mode）**按预设周期检查服务器并自动安装；**手动模式（Manual Mode）**由使用者发起查询，并在存在更新时决定立即还是稍后安装。实现见[示例主程序](https://github.com/zephyrproject-rtos/zephyr/blob/main/samples/subsys/mgmt/updatehub/src/main.c)。

## 25.2\_平台与网络边界

此移植最初针对[Freedom-K64F](https://docs.zephyrproject.org/latest/boards/nxp/frdm_k64f/doc/index.html#frdm_k64f)的以太网连接开发；具有相同连接能力的平台原则上可构建运行。示例还提供Wi-Fi、802.15.4和OpenThread的配置片段，但依赖对应硬件，片段以通用为目标，未针对所有平台充分优化。部分无线技术还需网关或 **边界路由器（Border Router）**，配置细节超出原文范围。

必须先确认 **片上系统（System on Chip，SoC）**和板卡支持MCUboot **引导加载程序（Bootloader）**。UpdateHub使用两个镜像槽完成升级，基础见[设备固件升级](P002_设备固件升级.md)。它作为Zephyr服务运行，依赖多个子系统，并通过 **用户数据报协议（User Datagram Protocol，UDP）**承载 **受限应用协议（Constrained Application Protocol，CoAP）**。

## 25.3\_工作区与引导程序

原文在终端1进入标准west工作区根目录，布局如下：

```shell
ls
bootloader  modules  tools  zephyr
```

> 译注：这里的 `bootloader`、`modules`、`tools`、`zephyr` 均为目录名称，组成上游工作区，不是某台机器的盘符路径，也不等于当前文档仓库的单目录结构。下面各构建目录相对于该工作区根目录；不要在未准备依赖的目录里假定这些路径已存在。

构建并烧录MCUboot：

```shell
west build -b frdm_k64f -d build/mcuboot-frdm_k64f bootloader/mcuboot/boot/zephyr
west flash -d build/mcuboot-frdm_k64f
```

## 25.4\_社区版服务器

默认配置使用 **社区版（Community Edition，CE）**UpdateHub-CE，需要自行运行服务器。它以Docker容器分发，可在本地网络或DigitalOcean、Vultr等托管环境运行。在终端2执行原命令：

```shell
docker run -it -p 8080:8080 -p 5683:5683/udp --rm
  updatehub/updatehub-ce:latest
```

> 译注：原命令把镜像名换到下一行却没有续行符；实际Shell中应将整条 `docker run` 命令及镜像名连为一行，或使用当前Shell的续行语法。该容器映射网页端口8080和UDP端口5683。

## 25.5\_云服务与证书

原文把[UpdateHub Cloud](https://updatehub.io/)描述为与社区版功能相近的企业方案，并将 **数据报传输层安全（Datagram Transport Layer Security，DTLS）**列为主要差别；云服务可选择是否使用受保护的CoAP（CoAPS）。这里保留原文的产品说明，不表示本次核验了当前服务套餐。

使用CoAPS/DTLS时加入 `overlay-dtls.conf`。可用示例证书测试，也可在Linux主机终端2用OpenSSL生成自己的证书。原例为：

```shell
openssl genrsa -out privkey.pem 512
openssl req -new -x509 -key privkey.pem -out servercert.pem
```

> 译注：原例使用512位RSA密钥，这是过时且不安全的长度，不应照此参数用于实际部署；当前加密库也可能拒绝它。此处保留历史命令作对照，实际证书应使用服务器和客户端共同支持的现代算法及密钥强度。RSA为以Rivest、Shamir和Adleman命名的非对称密码算法，不是产品型号。

证书和私钥需嵌入应用。原文称通过 `certificates.h` 引入，转换为 **唯一编码规则（Distinguished Encoding Rules，DER）**文件：

```shell
openssl x509 -in servercert.pem -outform DER -out servercert.der
openssl pkcs8 -topk8 -inform PEM -outform DER -nocrypt -in privkey.pem
  -out privkey.der
```

这里 **隐私增强邮件编码（Privacy-Enhanced Mail，PEM）**和DER是证书/密钥文件编码形式。原文第二条命令同样缺少跨行续行符，`-out privkey.der` 应属于同一命令。将DER文件放入示例证书目录；**译注：**本地版本实际为 `src/certificates/`，包含头为 `src/c_certificates.h`，应按实际源码核对原文简称。

使用云服务时，在自己的 `overlay-prj.conf` 中将Kconfig配置项 `CONFIG_UPDATEHUB_CE=n`。

## 25.6\_必要配置

| Kconfig配置项 | 用途 |
| --- | --- |
| [`CONFIG_UPDATEHUB_CE`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UPDATEHUB_CE) | `y` 选择社区版，`n` 选择云服务。 |
| [`CONFIG_UPDATEHUB_SERVER`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UPDATEHUB_SERVER) | 社区版服务器的IP地址或 **域名系统（Domain Name System，DNS）**名称；仅社区版有效。 |
| [`CONFIG_UPDATEHUB_POLL_INTERVAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UPDATEHUB_POLL_INTERVAL) | 轮询间隔，范围0至43200分钟（30天），默认1440分钟（24小时）。 |
| [`CONFIG_UPDATEHUB_PRODUCT_UID`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UPDATEHUB_PRODUCT_UID) | 产品标识；社区版示例值见 `overlay-prj.conf.example`。UID表示 **唯一标识符（Unique Identifier）**。 |

**译注：**先根据 `overlay-prj.conf.example` 创建自己的 `overlay-prj.conf`，再调整服务器和产品信息；不能把文件名占位当作已存在的配置。Kconfig片段的传入方式见[构建变量](https://docs.zephyrproject.org/latest/develop/application/index.html#important-build-vars)。

## 25.7\_以太网与Wi-Fi构建

原文构建命令以 `[ board_a | board_b ]` 表示任选一块板，**不是可直接输入Shell的方括号或管道表达式**，执行前须替换为一个实际板卡标识。

以下原命令的应用路径为 `samples/subsys/mgmt/updatehub`；若保持第25.3节的工作区根目录，必须把该参数改成 `zephyr/samples/subsys/mgmt/updatehub`。这样后续 `build/app` 和 `bootloader/mcuboot/` 才仍与工作区根一致。不要只在中途切入 `zephyr` 而忽略其他相对路径。

以太网只需要基础配置：

```shell
west build -b [ frdm_k64f | nucleo_f767zi ] -d build/app samples/subsys/mgmt/updatehub -- -DEXTRA_CONF_FILE=overlay-prj.conf
```

Wi-Fi增加 `overlay-wifi.conf`。示例通过 **扩展板（Shield）**和Arduino排针连接ESP-8266，详见[ESP-8266模块](https://docs.zephyrproject.org/latest/boards/shields/esp_8266/doc/index.html#module-esp-8266)：

```shell
west build -b [ frdm_k64f | nrf52840dk/nrf52840 | nucleo_f767zi ] --shield esp_8266_arduino -d build/app samples/subsys/mgmt/updatehub -- -DEXTRA_CONF_FILE="overlay-wifi.conf;overlay-prj.conf"
```

**原文注意：**板卡标识 `disco_l475_iot1` 不受此示例支持，原文说明其es-WIFI驱动当时不支持UDP；应按所用版本重新核对，不能将其当成所有后续版本的固定结论。

## 25.8\_实验性无线网络

**IEEE 802.15.4**分支使用 `overlay-802154.conf`。IEEE是 **电气与电子工程师协会（Institute of Electrical and Electronics Engineers）**。需要主机与被测设备两个节点，以及Linux 4.9或更新内核的完整 **低功耗无线个域网IPv6适配（IPv6 over Low-Power Wireless Personal Area Networks，6LoWPAN）**支持。原作者曾测试原生Linux驱动和ATUSB网关；完整支持超出其原文范围。

```shell
west build -b nrf52840dk/nrf52840 -d build/app samples/subsys/mgmt/updatehub -- -DEXTRA_CONF_FILE="overlay-802154.conf;overlay-prj.conf"
```

使用Atmel RF2XX扩展板的另一组目标：

```shell
west build -b [ frdm_k64f | nucleo_f767zi ] --shield atmel_rf2xx_arduino -d build/app samples/subsys/mgmt/updatehub -- -DEXTRA_CONF_FILE="overlay-802154.conf;overlay-prj.conf"
```

OpenThread分支使用 `overlay-ot.conf`，同样需要两个节点：主机侧 **网络协处理器（Network Co-Processor，NCP）**和被测设备。原验证环境是Linux 4.9或更新内核，可选 **IPv6/IPv4网络地址转换（Network Address Translation 64，NAT64）**，以[OpenThread边界路由器](https://openthread.io/guides/border-router)为起点。原作者用两块板在OpenThread 1.1.1的NCP模式下测试；这些是历史环境记录，不是本次验证结果。

```shell
west build -b nrf52840dk/nrf52840 -d build/app samples/subsys/mgmt/updatehub -- -DEXTRA_CONF_FILE="overlay-ot.conf;overlay-prj.conf"
```

## 25.9\_签名与烧录初始应用

初始应用负责连接服务器和查询更新，原例版本为1.0.0。应核对目标工具使用二进制 `.bin` 还是 **Intel十六进制文件（Intel HEX）**格式。使用west的 `sign` 命令和imgtool签名：

```text
west sign -t imgtool -d build/app -- --version 1.0.0 --pad
  --key bootloader/mcuboot/root-rsa-2048.pem

=== image configuration:
partition offset: 131072 (0x20000)
partition size: 393216 (0x60000)
rom start offset: 512 (0x200)
=== signing binaries
unsigned bin: build/app/zephyr/zephyr.bin
signed bin:   build/app/zephyr/zephyr.signed.bin
```

> 译注：原输出中的源码目录占位前缀已改为相对工作区的 `build/app/...`。分区偏移、大小与ROM起始偏移均为原例输出，不是HC32的分区参数；ROM指 **只读存储器（Read-Only Memory）**。公开的 `root-rsa-2048.pem` 是开发密钥，实际部署应替换为自己的密钥，见[镜像签名](P005_镜像签名.md)。

烧录签名应用：

```shell
west flash -d build/app --bin-file build/app/zephyr/zephyr.signed.bin
```

若目标使用HEX，原文给出的变体为 `west flash -d build/app --hex-file build/app/zephyr/zephyr.signed.hex`。

在终端3打开串口并按板卡复位键：

```shell
minicom -D /dev/ttyACM0
```

`/dev/ttyACM0` 是Linux串口设备节点，不是文档资源路径；应替换成系统实际识别的设备，Windows需使用对应串口工具和端口名称。

## 25.10\_签名测试镜像

测试镜像使用版本2.0.0，签名参数与初始填充镜像不同：

```text
west sign --no-hex --bin -B build/zephyr-2.0.0.bin -t imgtool -d build/app --
  --version 2.0.0 --key bootloader/mcuboot/root-rsa-2048.pem

=== image configuration:
partition offset: 131072 (0x20000)
partition size: 393216 (0x60000)
rom start offset: 512 (0x200)
=== signing binaries
unsigned bin: build/app/zephyr/zephyr.bin
signed bin:   build/zephyr-2.0.0.bin
```

原命令在 `--` 后换行却没有续行符，实际执行时须连成一条命令。**译注：**此处复用已有未签名应用，改变签名镜像头里的版本；若还要修改应用功能，必须先构建对应的新代码。输出中的目录前缀同样改为相对路径。

## 25.11\_生成UpdateHub包

原文安装 **UpdateHub工具集（UpdateHub Utilities，uhu）**：

```shell
pip3 install --user uhu
```

设置产品标识。社区版示例值见 `overlay-prj.conf.example`，云服务值从其网页界面取得；以下为原公开示例值：

```shell
uhu product use "e4d37cfe6ec48a2d069cc0bbb8b078677e9a0d8df3a027c4d8ea131130c4265f"
```

加入文件并选择 `zephyr` 模式：

```shell
uhu package add build/zephyr-2.0.0.bin -m zephyr
```

指定包版本：

```shell
uhu package version 2.0.0
```

生成归档：

```shell
uhu package archive --output build/zephyr-2.0.0.pkg
```

后续网页操作针对社区版；云服务按[其官方文档](https://docs.updatehub.io/)操作。

## 25.12\_上传包、注册设备与发布分发

打开 `<your-ip-address>:8080`，原社区版默认用户名、密码均为示例值 `admin`。进入包菜单，点击 **上传包（UPLOAD PACKAGE）**，选择上一步生成的包。

手动模式在设备终端3注册并查询：

```shell
updatehub run
```

正常时输出 `No update available`（没有可用更新）。轮询模式在Kconfig配置项 [`CONFIG_UPDATEHUB_POLL_INTERVAL`](https://docs.zephyrproject.org/latest/kconfig.html#CONFIG_UPDATEHUB_POLL_INTERVAL) 指定时间后自动注册，也可用上述命令提前查询。

`Could not receive data`（无法接收数据）表示应用未能访问服务器，常见原因是服务器未运行、缺少网络路由，或忘记修改 `overlay-prj.conf`。

在服务器 **分发（Rollout）**菜单点击 **创建分发（CREATE ROLLOUT）**，选择已上传包的版本。完成后更新被发布，服务器可响应设备的更新请求。

## 25.13\_运行更新与重启

回到设备终端再次输入：

```shell
updatehub run
```

设备查询服务器并下载更新包。成功时输出 `Image flashed successfully, you can reboot now`（镜像已成功写入，可以重启）。轮询模式会自动重启，可跳过手动重启；手动模式输入：

```shell
kernel reboot cold
```

启动新镜像后，设备再次查询服务器，原文预期输出 `No update available`。检查版本的原命令与输出为：

```text
uart:~$ updatehub info
Unique device id: acbdef0123456789
Firmware Version: 2.0.0
Product uid: e4d37cfe6ec48a2d069cc0bbb8b078677e9a0d8df3a027c4d8ea131130c4265f
UpdateHub Server: <server ip/dns>
uart:~$
```

## 25.14\_原作者使用的硬件

下表是原UpdateHub团队记录，不是本次实测。**调制解调器（Modem）**一行采用 **点对点协议（Point-to-Point Protocol，PPP）**。

| 原接口编号 | 网络接口 | 扩展板或设备 |
| --- | --- | --- |
| 1 | 以太网（Ethernet）。 | 板载。 |
| 2 | Wi-Fi。 | ESP-8266。 |
| 3 | Modem，PPP。 | SIMCOM 808。 |
| 4 | IEEE 802.15.4，6LoWPAN。 | 板载或RF2XX。 |
| 6 | OpenThread网络。 | 板载。 |

| 开发板 | 原表网络接口编号 |
| --- | --- |
| FRDM-K64F | 1、2、3、4。 |
| nRF52840 DK | 2、3、4、5、6。 |
| Nucleo F767ZI | 1、2、3、4。 |

**译注：**原接口表没有编号5，而nRF52840行包含5；此处原样保留，不臆造其网络类型。更多接口见[UpdateHub空中升级API](P031_UpdateHub接口.md)，API为 **应用程序编程接口（Application Programming Interface）**。

[上一章：hawkBit升级示例](P024_hawkBit升级示例.md) · [下一章：OSDP设备协议示例](P026_OSDP设备协议示例.md) · [返回大纲](大纲.md)
