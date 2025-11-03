import { gql } from "@apollo/client";
import client from "./apollo";

const GET_ALL = gql`query { getAllMusic { id title artist genre userId } }`;
const CREATE = gql`
  mutation($music: MusicInput!, $userId: Int!) {
    createMusic(music: $music, userId: $userId) {
      id title artist genre userId
    }
  }`;
const UPDATE = gql`
  mutation($id: Int!, $music: MusicInput!) {
    updateMusic(id: $id, music: $music) {
      id title artist genre userId
    }
  }`;
const DELETE = gql`mutation($id: Int!) { deleteMusic(id: $id) }`;

export const musicGraphQLService = {
  async getAll() {
    const { data } = await client.query({ query: GET_ALL, fetchPolicy: "no-cache" });
    return data.getAllMusic;
  },
  async create(payload, userId = 1) {
    await client.mutate({ mutation: CREATE, variables: { music: payload, userId } });
  },
  async update(id, payload) {
    await client.mutate({ mutation: UPDATE, variables: { id, music: payload } });
  },
  async delete(id) {
    await client.mutate({ mutation: DELETE, variables: { id } });
  },
  getId(m) { return m.id; }
};
