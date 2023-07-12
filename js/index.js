import * as dotenv from "dotenv";
import blue from "@atproto/api";

dotenv.config();
const { BskyAgent } = blue;

const postCapy = async () => {
  const { RichText } = blue;
  const agent = new BskyAgent({ service: "https://bsky.social/" });
  await agent.login({
    identifier: process.env.BLUESKY_BOT_EMAIL,
    password: process.env.BLUESKY_BOT_PASSWORD,
  });
  const rt = new RichText({ text: "Do you have an orange for my head?" });
  const postRecord = {
    $type: "app.bsky.feed.post",
    text: rt.text,
    facets: rt.facets,
    createdAt: new Date().toISOString(),
  };
  await agent.post(postRecord);
};

postCapy();
