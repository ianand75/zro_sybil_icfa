import axios from "axios";
import { addNewRecord, delay, persistRecords, readRecords } from "mini-task-clirunner";
import fs from "fs";

const urls = {
  op: `https://api-optimistic.etherscan.io/api?module=account&action=txlistinternal&apikey=Y73BTMEK5331XBN3P6S44XVHBD7HANT9P2&txhash=`,
  arb: `https://api.arbiscan.io/api?module=account&action=txlistinternal&apikey=5XPH7331JX8T3H4412QWCC5YMNM3N88FRF&txhash=`,
  polygon: `https://api.polygonscan.com/api?module=account&action=txlistinternal&apikey=D7VCGJA2IDPQ151KX56TE9G6KVECBIH22X&txhash=`,
  celo: `https://api.celoscan.io/api?module=account&action=txlistinternal&apikey=S5ZJ6CNE15JZ2DDFMP4MXQAVWQXUBMNBKP&txhash=`,
  bsc: `https://api.bscscan.com/api?module=account&action=txlistinternal&apikey=J7G5RYEQZBII4RQ6EK3ABM1BKJF98KCYH2&txhash=`,
  fantom: `https://api.ftmscan.com/api?module=account&action=txlistinternal&apikey=UNM3VIKXU5R4F4CUA7M2VT4EMQZ8YEMAWS&txhash=`,
};

const fundThresholds = {
  op: 0.5,
  arb: 0.5,
  polygon: 100,
  celo: 5,
  bsc: 5,
  mr: 10,
  gnosis: 100,
  fantom: 200,
};

(async () => {
  console.log(process.argv);

  const input = process.argv[2];
  const output = process.argv[3];
  const network = process.argv[4];

  if (!network) throw new Error("");

  const url = urls[network];

  // const abspath =
  const trans = require(input);
  const thresold = fundThresholds[network];

  let result = [];
  for (const tr of trans) {
    console.log("tr", tr);

    const value = parseFloat(tr.value);
    if (value > thresold) {
      //   console.log(tr);
      try {
        const res = await axios.get(url + tr.hash);

        //   console.log(res);
        const internalTrans = res.data.result;

        // for (const itran of internalTrans) {
        //   await addNewRecord(output, { tx: tr.Txhash, from: tr.From, to: itran.to, value: itran.value });
        // }

        const rs = internalTrans.map((i) => ({ tx: tr.hash, from: tr.from, to: i.to, value: i.value }));

        result = result.concat(rs);
      } catch (error) {
        console.log(error);
      }

      await delay(1000);
    }

    //
  }

  const headers = [
    { id: "tx", title: "tx" },
    { id: "from", title: "from" },
    { id: "to", title: "to" },
    { id: "value", title: "value" },
  ];
  await persistRecords(output, headers, result);
})();
