export interface IMessage {
    id: number
    createdAt: Date
    createdBy: number
    content: string
    chatID: number
}

export interface IChatItem {
    id: number
    createdAt: Date
    createdBy: number
    name: string
    lastMessage: IMessage
}