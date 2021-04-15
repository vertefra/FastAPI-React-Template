import { Method } from 'axios';

export interface Request {
	method: Method;
	url: string;
	payload?: object;
}
