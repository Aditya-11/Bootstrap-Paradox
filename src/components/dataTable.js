let table = 
`<table class="dataframe table table-borderless table-striped table-hover">
<thead>
  <tr style="text-align: right;">
    <th></th>
    <th>commodity</th>
    <th>supplier</th>
    <th>Model_id</th>
    <th>price_in_dollars</th>
    <th>supplier_rating</th>
    <th>component_rating</th>
    <th>rating</th>
  </tr>
</thead>
<tbody>
  <tr>
    <th>164</th>
    <td>Keyboard</td>
    <td>Silicon Power</td>
    <td>651759</td>
    <td>12.0</td>
    <td>8</td>
    <td>6</td>
    <td>300.8</td>
  </tr>
  <tr>
    <th>317</th>
    <td>Mouse</td>
    <td>Transcend Information</td>
    <td>410641</td>
    <td>14.0</td>
    <td>7</td>
    <td>9</td>
    <td>298.0</td>
  </tr>
  <tr>
    <th>191</th>
    <td>DVDdrive</td>
    <td>Promise Technology</td>
    <td>371436</td>
    <td>32.0</td>
    <td>5</td>
    <td>3</td>
    <td>299.2</td>
  </tr>
  <tr>
    <th>90</th>
    <td>RAM8GB</td>
    <td>Seasonic</td>
    <td>890450</td>
    <td>50.0</td>
    <td>6</td>
    <td>4</td>
    <td>294.8</td>
  </tr>
  <tr>
    <th>67</th>
    <td>MotherBoard</td>
    <td>LaCie</td>
    <td>691072</td>
    <td>51.0</td>
    <td>4</td>
    <td>7</td>
    <td>292.2</td>
  </tr>
  <tr>
    <th>28</th>
    <td>HDD500GB</td>
    <td>AOpen</td>
    <td>356250</td>
    <td>53.0</td>
    <td>5</td>
    <td>8</td>
    <td>291.0</td>
  </tr>
  <tr>
    <th>211</th>
    <td>Chasis</td>
    <td>ADATA</td>
    <td>743233</td>
    <td>54.0</td>
    <td>7</td>
    <td>9</td>
    <td>290.0</td>
  </tr>
  <tr>
    <th>406</th>
    <td>Speaker</td>
    <td>Toshiba</td>
    <td>874863</td>
    <td>60.0</td>
    <td>8</td>
    <td>3</td>
    <td>293.6</td>
  </tr>
  <tr>
    <th>350</th>
    <td>Monitor</td>
    <td>Western Digital</td>
    <td>936522</td>
    <td>80.0</td>
    <td>7</td>
    <td>5</td>
    <td>288.0</td>
  </tr>
  <tr>
    <th>147</th>
    <td>RAM16GB</td>
    <td>AMAX Information Technologies</td>
    <td>888670</td>
    <td>83.0</td>
    <td>5</td>
    <td>4</td>
    <td>288.2</td>
  </tr>
  <tr>
    <th>280</th>
    <td>PSU400</td>
    <td>Shuttle SilverStoneTechnology</td>
    <td>888380</td>
    <td>86.0</td>
    <td>9</td>
    <td>6</td>
    <td>286.0</td>
  </tr>
  <tr>
    <th>49</th>
    <td>CPU</td>
    <td>Verbatim Corporation</td>
    <td>329203</td>
    <td>112.0</td>
    <td>8</td>
    <td>7</td>
    <td>280.0</td>
  </tr>
  <tr>
    <th>257</th>
    <td>PSU800</td>
    <td>Transcend Information</td>
    <td>311697</td>
    <td>152.0</td>
    <td>5</td>
    <td>8</td>
    <td>271.2</td>
  </tr>
  <tr>
    <th>386</th>
    <td>GraphicCard</td>
    <td>ACubeSystems</td>
    <td>538817</td>
    <td>153.0</td>
    <td>5</td>
    <td>9</td>
    <td>270.2</td>
  </tr>
</tbody>
</table>`

let render = (template, node) => {
    if(!node)
        return;
    node.innerHTML = template
}

let sum = (num) => num+10;

export {table, render, sum};