---
id: learning.zephyr-docs.boards-shields.page-140
title: NXP S32K5XX-MB Shield
kind: reference
status: maintained
domains: [zephyr, boards]
source_url: https://docs.zephyrproject.org/latest/boards/shields/nxp_s32k5xx_mb/doc/index.html
---

<!-- Copyright 2015-2026 Zephyr Project members and individual contributors. -->
<!-- SPDX-License-Identifier: Apache-2.0 -->
<!-- 中文翻译；编号、导航与译注为本地新增。 -->

<a id="nxp-s32k5xx-mb-shield"></a>

<a id="nxp-s32k5xx-mb"></a>

# 第140章\_NXP S32K5XX-MB扩展板（Shield）

原文：[官方页面](https://docs.zephyrproject.org/latest/boards/shields/nxp_s32k5xx_mb/doc/index.html)。读取日期：2026-10-16；来源摘要见[来源记录](../SOURCES.md)。

<a id="overview"></a>

## 概述（Overview）

此Zephyr扩展板即NXP S32K5XX主板，可增加[S32K5XXCVB](../boards_nxp_remaining/P012_S32K5XXCVB.md#s32k5xxcvb)的I/O连接能力。

<a id="gpio-pin-matrix"></a>

## GPIO引脚矩阵（Pin Matrix）

原理图中Jxxx符号与PCB布局GPIO引脚矩阵的对应关系见下表。

<table>
<tr>
<th></th>
<th>1</th>
<th>2</th>
<th>3</th>
<th>4</th>
<th>5</th>
<th>6</th>
<th>7</th>
<th>8</th>
<th>9</th>
<th>10</th>
</tr>
<tr>
<td>A</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>J207</td>
<td>J173</td>
<td>J139</td>
<td>J447</td>
</tr>
<tr>
<td>B</td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td></td>
<td>J208</td>
<td>J174</td>
<td>J140</td>
<td>J105</td>
</tr>
<tr>
<td>C</td>
<td>J404</td>
<td>J370</td>
<td>J338</td>
<td>J305</td>
<td>J273</td>
<td>J241</td>
<td>J209</td>
<td>J175</td>
<td>J141</td>
<td>J106</td>
</tr>
<tr>
<td>D</td>
<td>J405</td>
<td>J371</td>
<td>J339</td>
<td>J306</td>
<td>J274</td>
<td>J242</td>
<td>J210</td>
<td>J176</td>
<td>J142</td>
<td>J107</td>
</tr>
<tr>
<td>E</td>
<td>J406</td>
<td>J372</td>
<td>J340</td>
<td>J307</td>
<td>J275</td>
<td>J243</td>
<td>J211</td>
<td>J177</td>
<td>J143</td>
<td>J108</td>
</tr>
<tr>
<td>F</td>
<td>J407</td>
<td>J373</td>
<td>J341</td>
<td>J308</td>
<td>J276</td>
<td>J244</td>
<td>J212</td>
<td>J178</td>
<td>J144</td>
<td>J109</td>
</tr>
<tr>
<td>G</td>
<td>J408</td>
<td>J374</td>
<td>J342</td>
<td>J309</td>
<td>J277</td>
<td>J245</td>
<td>J213</td>
<td>J179</td>
<td>J145</td>
<td>J110</td>
</tr>
<tr>
<td>H</td>
<td>J409</td>
<td>J375</td>
<td>J343</td>
<td>J310</td>
<td>J278</td>
<td>J246</td>
<td>J214</td>
<td>J180</td>
<td>J146</td>
<td>J111</td>
</tr>
<tr>
<td>输入（I）</td>
<td>J410</td>
<td>J376</td>
<td>J344</td>
<td>J311</td>
<td>J279</td>
<td>J247</td>
<td>J215</td>
<td>J181</td>
<td>J147</td>
<td>J112</td>
</tr>
<tr>
<td>J</td>
<td>J411</td>
<td>J377</td>
<td>J345</td>
<td>J312</td>
<td>J280</td>
<td>J248</td>
<td>J216</td>
<td>J182</td>
<td>J148</td>
<td>J113</td>
</tr>
<tr>
<td>K</td>
<td>J412</td>
<td>J378</td>
<td>J346</td>
<td>J313</td>
<td>J281</td>
<td>J249</td>
<td>J217</td>
<td>J183</td>
<td>J149</td>
<td>J114</td>
</tr>
<tr>
<td>L</td>
<td>J413</td>
<td>J379</td>
<td>J347</td>
<td>J314</td>
<td>J282</td>
<td>J250</td>
<td>J218</td>
<td>J184</td>
<td>J150</td>
<td>J115</td>
</tr>
<tr>
<td>M</td>
<td>J414</td>
<td>J380</td>
<td>J348</td>
<td>J315</td>
<td>J283</td>
<td>J251</td>
<td>J219</td>
<td>J185</td>
<td>J151</td>
<td>J116</td>
</tr>
<tr>
<td>N</td>
<td>J415</td>
<td>J381</td>
<td>J349</td>
<td>J316</td>
<td>J284</td>
<td>J252</td>
<td>J220</td>
<td>J186</td>
<td>J152</td>
<td>J117</td>
</tr>
<tr>
<td>输出（O）</td>
<td>J416</td>
<td>J382</td>
<td>J350</td>
<td>J317</td>
<td>J285</td>
<td>J253</td>
<td>J221</td>
<td>J187</td>
<td>J153</td>
<td>J118</td>
</tr>
<tr>
<td>P</td>
<td>J417</td>
<td>J383</td>
<td>J351</td>
<td>J318</td>
<td>J286</td>
<td>J254</td>
<td>J222</td>
<td>J188</td>
<td>J154</td>
<td>J119</td>
</tr>
<tr>
<td>Q</td>
<td>J418</td>
<td>J384</td>
<td>J352</td>
<td>J319</td>
<td>J287</td>
<td>J255</td>
<td>J223</td>
<td>J189</td>
<td>J155</td>
<td>J120</td>
</tr>
<tr>
<td>R</td>
<td>J419</td>
<td>J385</td>
<td>J353</td>
<td>J320</td>
<td>J288</td>
<td>J256</td>
<td>J224</td>
<td>J190</td>
<td>J156</td>
<td>J121</td>
</tr>
<tr>
<td>安全态（S）</td>
<td>J420</td>
<td>J386</td>
<td>J354</td>
<td>J321</td>
<td>J289</td>
<td>J257</td>
<td>J225</td>
<td>J191</td>
<td>J157</td>
<td>J122</td>
</tr>
<tr>
<td>T</td>
<td>J421</td>
<td>J387</td>
<td>J355</td>
<td>J322</td>
<td>J290</td>
<td>J258</td>
<td>J226</td>
<td>J192</td>
<td>J158</td>
<td>J123</td>
</tr>
<tr>
<td>U</td>
<td>J422</td>
<td>J388</td>
<td>J356</td>
<td>J323</td>
<td>J291</td>
<td>J259</td>
<td>J227</td>
<td>J193</td>
<td>J159</td>
<td>J124</td>
</tr>
<tr>
<td>V</td>
<td>J423</td>
<td>J389</td>
<td>J357</td>
<td>J324</td>
<td>J292</td>
<td>J260</td>
<td>J228</td>
<td>J194</td>
<td>J160</td>
<td>J125</td>
</tr>
<tr>
<td>W</td>
<td>J424</td>
<td>J390</td>
<td>J358</td>
<td>J325</td>
<td>J293</td>
<td>J261</td>
<td>J229</td>
<td>J195</td>
<td>J161</td>
<td>J126</td>
</tr>
<tr>
<td>X</td>
<td>J425</td>
<td>J391</td>
<td>J359</td>
<td>J326</td>
<td>J294</td>
<td>J262</td>
<td>J230</td>
<td>J196</td>
<td>J162</td>
<td>J127</td>
</tr>
<tr>
<td>Y</td>
<td>J426</td>
<td>J392</td>
<td>J360</td>
<td>J327</td>
<td>J295</td>
<td>J263</td>
<td>J231</td>
<td>J197</td>
<td>J163</td>
<td>J128</td>
</tr>
<tr>
<td>Z</td>
<td>J427</td>
<td>J393</td>
<td>J361</td>
<td>J328</td>
<td>J296</td>
<td>J264</td>
<td>J232</td>
<td>J198</td>
<td>J164</td>
<td>J129</td>
</tr>
<tr>
<td>AA</td>
<td>J428</td>
<td>J394</td>
<td>J362</td>
<td>J329</td>
<td>J297</td>
<td>J265</td>
<td>J233</td>
<td>J199</td>
<td>J165</td>
<td>J130</td>
</tr>
<tr>
<td>AB</td>
<td>J429</td>
<td>J395</td>
<td>J363</td>
<td>J330</td>
<td>J298</td>
<td>J266</td>
<td>J234</td>
<td>J200</td>
<td>J166</td>
<td>J131</td>
</tr>
<tr>
<td>AC</td>
<td>J430</td>
<td>J396</td>
<td>J364</td>
<td>J331</td>
<td>J299</td>
<td>J267</td>
<td>J235</td>
<td>J201</td>
<td>J167</td>
<td>J132</td>
</tr>
<tr>
<td>AD</td>
<td>J431</td>
<td>J397</td>
<td>J365</td>
<td>J332</td>
<td>J300</td>
<td>J268</td>
<td>J236</td>
<td>J202</td>
<td>J168</td>
<td>J133</td>
</tr>
<tr>
<td>AE</td>
<td>J432</td>
<td>J398</td>
<td>J366</td>
<td>J333</td>
<td>J301</td>
<td>J269</td>
<td>J237</td>
<td>J203</td>
<td>J169</td>
<td>J134</td>
</tr>
<tr>
<td>AF</td>
<td>J433</td>
<td>J399</td>
<td>J367</td>
<td>J334</td>
<td>J302</td>
<td>J270</td>
<td>J238</td>
<td>J204</td>
<td>J170</td>
<td>J135</td>
</tr>
<tr>
<td>AG</td>
<td>J434</td>
<td>J400</td>
<td>J368</td>
<td>J335</td>
<td>J303</td>
<td>J271</td>
<td>J239</td>
<td>J205</td>
<td>J171</td>
<td>J136</td>
</tr>
<tr>
<td>AH</td>
<td>J435</td>
<td>J401</td>
<td>J369</td>
<td>J336</td>
<td>J304</td>
<td>J272</td>
<td>J240</td>
<td>J206</td>
<td>J172</td>
<td>J137</td>
</tr>
<tr>
<td>AI</td>
<td>J437</td>
<td>J438</td>
<td>J439</td>
<td>J440</td>
<td>J441</td>
<td>J442</td>
<td>J443</td>
<td>J444</td>
<td>J445</td>
<td>J446</td>
</tr>
</table>

<a id="set-up-the-board"></a>

### 设置开发板（Set-up the Board）

首先确认主板已正确连接[S32K5XXCVB](../boards_nxp_remaining/P012_S32K5XXCVB.md#s32k5xxcvb)。

需要USB转串口器，例如CH340，才能查看串口输出，按下图连接：

<table>
<tr>
<th>CH340转换器引脚</th>
<th>GPIO引脚矩阵（Pin Matrix）</th>
</tr>
<tr>
<td>发送数据（TXD）</td>
<td>O5</td>
</tr>
<tr>
<td>接收数据（RXD）</td>
<td>P5</td>
</tr>
<tr>
<td>地（GND）</td>
<td>AI10</td>
</tr>
</table>

<a id="id2"></a>

运行终端程序接收输出，例如跨平台[pySerial miniterm](https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm)终端[注1](#id1)：

```text
python -m serial.tools.miniterm <port> 115200
```

将`<port>`替换成开发板对应端口，例如Linux下的/dev/ttyUSB0。

<a id="programming"></a>

## 编程（Programming）

调用west build时，通过--shield <option>选择以下支持的扩展板：


- `nxp_s32k5xx_mb`

例如：

```text
# From the root of the zephyr repository
west build -b s32k5xxcvb/s32k566/m7 --shield nxp_s32k5xx_mb samples/hello_world
west flash
```

终端中应出现以下消息：

```text
Hello World! s32k5xxcvb/s32k566/m7
```

<a id="references"></a>

## 参考资料（References）

<a id="id1"></a>

〔[1](#id2)〕 [https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm](https://pyserial.readthedocs.io/en/latest/tools.html#module-serial.tools.miniterm)

---

[上一章](P139_NXP_MX9_DSI_OLED_Panel.md) · [返回大纲](大纲.md) · [全站翻译进度](../PROGRESS.md) · [下一章](P141_OD-6010_SLCD_Panel_Shield.md)
